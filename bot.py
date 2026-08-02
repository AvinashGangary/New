import os
import sys
import asyncio
import time
import json
import logging
import random
import re
import requests
import traceback
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import pytz

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram.constants import ParseMode

BOT_TOKEN = "7477846047:AAHHf_azJ_dVfmy97yc7FU6t4ko6CGIR6Bs"
ADMIN_ID = 6824982812
LOGS_CHANNEL_ID = -100

SCRIPT_DIR = Path(__file__).parent.absolute()
USERS_FILE = SCRIPT_DIR / "approved_users.json"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

class DataManager:
    @staticmethod
    def load_json(file_path: Path) -> dict:
        if file_path.exists():
            try:
                with open(file_path, 'r') as f: return json.load(f)
            except: return {}
        return {}
    
    @staticmethod
    def is_approved(user_id: int) -> bool:
        users = DataManager.load_json(USERS_FILE)
        return user_id == ADMIN_ID or str(user_id) in users

class FacebookAutomation:
    def __init__(self):
        self.api_base = "http://72.60.39.128:4500"
        self.driver = None

    def get_temp_email(self) -> Tuple[Optional[str], Optional[str]]:
        try:
            response = requests.get(f"{self.api_base}/create", timeout=20)
            res = response.json()
            if "address" in res: return res["address"], res["token"]
            inner_str = res.get("details", {}).get("details", {}).get("response", "{}")
            inner = json.loads(inner_str)
            return inner.get("address"), inner.get("token")
        except: return None, None

    async def create_account(self, f_name, l_name):
        email, token = self.get_temp_email()
        if not email: return None
        
        try:
            opts = Options()
            opts.add_argument("--headless=new")
            opts.add_argument("--no-sandbox")
            opts.add_argument("--disable-dev-shm-usage")
            opts.add_argument("--window-size=1920,1080")
            opts.add_argument("--disable-blink-features=AutomationControlled")
            opts.add_experimental_option("excludeSwitches", ["enable-automation"])
            opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
            
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
            wait = WebDriverWait(self.driver, 35)
            
            self.driver.get("https://www.facebook.com/r.php")
            
          
            wait.until(EC.visibility_of_element_located((By.NAME, "firstname"))).send_keys(f_name)
            self.driver.find_element(By.NAME, "lastname").send_keys(l_name)
            
            em_field = self.driver.find_element(By.NAME, "reg_email__")
            for char in email:
                em_field.send_keys(char)
                await asyncio.sleep(0.05)
            em_field.send_keys(Keys.TAB)
            
            try:
                conf = wait.until(EC.visibility_of_element_located((By.NAME, "reg_email_confirmation__")))
                conf.send_keys(email)
            except: pass

            Select(self.driver.find_element(By.ID, "year")).select_by_value("2002")
            self.driver.find_element(By.NAME, "reg_passwd__").send_keys("Tg_Soulcrack@12")
            self.driver.find_element(By.CSS_SELECTOR, 'input[name="sex"][value="2"]').click()
            
            await asyncio.sleep(2)
            self.driver.find_element(By.NAME, "websubmit").click()

          
            otp = None
            start_poll = time.time()
            while time.time() - start_poll < 180:
                try:
                    r = requests.get(f"{self.api_base}/check/{token}", timeout=15).json()
                    for m in r.get("emails", []):
                        match = re.search(r"FB-(\d{5})", m.get("body", ""))
                        if match: 
                            otp = match.group(1)
                            break
                    if otp: break
                    await asyncio.sleep(10)
                except: await asyncio.sleep(10)

            if not otp: return None

            otp_in = wait.until(EC.visibility_of_element_located((By.ID, "code_in_cliff")))
            otp_in.send_keys(otp)
            self.driver.find_element(By.NAME, "confirm").click()
            await asyncio.sleep(5)
            
          
            ist = pytz.timezone('Asia/Kolkata')
            created_at = datetime.now(ist).strftime("%Y-%m-%d %I:%M:%S %p %Z")

            return {
                "username": f"{f_name} {l_name}",
                "email": email,
                "password": "Tg_Soulcrack@12",
                "token": token,
                "created_at": created_at
            }
        except: return None
        finally:
            if self.driver: self.driver.quit()

async def create_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not DataManager.is_approved(update.effective_user.id):
        return await update.message.reply_text("❌ Not authorized.")
    
    try:
        count = int(context.args[0])
    except:
        return await update.message.reply_text("Usage: /create <number>")
    
    status = await update.message.reply_text(f"🚀 Starting {count} accounts...")
    auto = FacebookAutomation()
    
    
    first_names = ["Richard", "John", "David", "Michael", "James", "Robert"]
    last_names = ["Garcia", "Smith", "Johnson", "Williams", "Brown"]

    for i in range(1, count + 1):
        f_name = random.choice(first_names)
        l_name = random.choice(last_names)
        
        await status.edit_text(f"⏳ Creating account {i}/{count}...")
        res = await auto.create_account(f_name, l_name)
        
        if res:

            msg = (
                f"✅ Account #{i} Created Successfully!\n\n"
                f"👤 Username: {res['username']}\n"
                f"📧 Email: `{res['email']}`\n"
                f"🔑 Password: `{res['password']}`\n"
                f"🎫 Mail Token: `{res['token']}`\n"
                f"🕐 Created: {res['created_at']}"
            )
            await update.message.reply_text(msg, parse_mode=ParseMode.MARKDOWN)
            
          
            try:
                await context.bot.send_message(LOGS_CHANNEL_ID, f"📊 Logs: New Account Created\nUser: {res['username']}\nEmail: {res['email']}")
            except: pass
        else:
            await update.message.reply_text(f"❌ Failed Account #{i}")
        
        await asyncio.sleep(5)
        
    await status.edit_text("🎉 Account creation process finished.")

def main():
    app = Application.builder().token(BOT_TOKEN).connect_timeout(60).read_timeout(60).build()
    app.add_handler(CommandHandler("create", create_cmd))
    print("🚀 Bot started. Ready for creation.")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
