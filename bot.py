pipelines:
  custom:
    run-manual:
      - parallel:
          - step:
              name: Runner 1
              image: python:3.10
              script:
                - chmod +x mustafa || true
                - python3 main.py $IP $PORT $DURATION $PACKET_SIZE $THREADS
          - step:
              name: Runner 2
              image: python:3.10
              script:
                - chmod +x mustafa || true
                - python3 main.py $IP $PORT $DURATION $PACKET_SIZE $THREADS
          - step:
              name: Runner 3
              image: python:3.10
              script:
                - chmod +x mustafa || true
                - python3 main.py $IP $PORT $DURATION $PACKET_SIZE $THREADS
          - step:
              name: Runner 4
              image: python:3.10
              script:
                - chmod +x mustafa || true
                - python3 main.py $IP $PORT $DURATION $PACKET_SIZE $THREADS
          - step:
              name: Runner 5
              image: python:3.10
              script:
                - chmod +x mustafa || true
                - python3 main.py $IP $PORT $DURATION $PACKET_SIZE $THREADS
          - step:
              name: Runner 6
              image: python:3.10
              script:
                - chmod +x mustafa || true
                - python3 main.py $IP $PORT $DURATION $PACKET_SIZE $THREADS
          - step:
              name: Runner 7
              image: python:3.10
              script:
                - chmod +x mustafa || true
                - python3 main.py $IP $PORT $DURATION $PACKET_SIZE $THREADS
          - step:
              name: Runner 8
              image: python:3.10
              script:
                - chmod +x mustafa || true
                - python3 main.py $IP $PORT $DURATION $PACKET_SIZE $THREADS
          - step:
              name: Runner 9
              image: python:3.10
              script:
                - chmod +x mustafa || true
                - python3 main.py $IP $PORT $DURATION $PACKET_SIZE $THREADS
          - step:
              name: Runner 10
              image: python:3.10
              script:
                - chmod +x mustafa || true
                - python3 main.py $IP $PORT $DURATION $PACKET_SIZE $THREADS

          # 👇 SAME PATTERN CONTINUES 👇

          - step: { name: Runner 11, image: python:3.10, script: [ "chmod +x mustafa || true", "python3 main.py $IP $PORT $DURATION $PACKET_SIZE $THREADS" ] }
          - step: { name: Runner 12, image: python:3.10, script: [ "chmod +x mustafa || true", "python3 main.py $IP $PORT $DURATION $PACKET_SIZE $THREADS" ] }
          - step: { name: Runner 13, image: python:3.10, script: [ "chmod +x mustafa || true", "python3 main.py $IP $PORT $DURATION $PACKET_SIZE $THREADS" ] }
          - step: { name: Runner 14, image: python:3.10, script: [ "chmod +x mustafa || true", "python3 main.py $IP $PORT $DURATION $PACKET_SIZE $THREADS" ] }
          - step: { name: Runner 15, image: python:3.10, script: [ "chmod +x mustafa || true", "python3 main.py $IP $PORT $DURATION $PACKET_SIZE $THREADS" ] }
          - step: { name: Runner 16, image: python:3.10, script: [ "chmod +x mustafa || true", "python3 main.py $IP $PORT $DURATION $PACKET_SIZE $THREADS" ] }
          - step: { name: Runner 17, image: python:3.10, script: [ "chmod +x mustafa || true", "python3 main.py $IP $PORT $DURATION $PACKET_SIZE $THREADS" ] }
          - step: { name: Runner 18, image: python:3.10, script: [ "chmod +x mustafa || true", "python3 main.py $IP $PORT $DURATION $PACKET_SIZE $THREADS" ] }
          - step: { name: Runner 19, image: python:3.10, script: [ "chmod +x mustafa || true", "python3 main.py $IP $PORT $DURATION $PACKET_SIZE $THREADS" ] }
          - step: { name: Runner 20, image: python:3.10, script: [ "chmod +x mustafa || true", "python3 main.py $IP $PORT $DURATION $PACKET_SIZE $THREADS" ] }

          - step: { name: Runner 21, image: python:3.10, script: [ "chmod +x mustafa || true", "python3 main.py $IP $PORT $DURATION $PACKET_SIZE $THREADS" ] }
          - step: { name: Runner 22, image: python:3.10, script: [ "chmod +x mustafa || true", "python3 main.py $IP $PORT $DURATION $PACKET_SIZE $THREADS" ] }
          - step: { name: Runner 23, image: python:3.10, script: [ "chmod +x mustafa || true", "python3 main.py $IP $PORT $DURATION $PACKET_SIZE $THREADS" ] }
          - step: { name: Runner 24, image: python:3.10, script: [ "chmod +x mustafa || true", "python3 main.py $IP $PORT $DURATION $PACKET_SIZE $THREADS" ] }
          - step: { name: Runner 25, image: python:3.10, script: [ "chmod +x mustafa || true", "python3 main.py $IP $PORT $DURATION $PACKET_SIZE $THREADS" ] }
          - step: { name: Runner 26, image: python:3.10, script: [ "chmod +x mustafa || true", "python3 main.py $IP $PORT $DURATION $PACKET_SIZE $THREADS" ] }
          - step: { name: Runner 27, image: python:3.10, script: [ "chmod +x mustafa || true", "python3 main.py $IP $PORT $DURATION $PACKET_SIZE $THREADS" ] }
          - step: { name: Runner 28, image: python:3.10, script: [ "chmod +x mustafa || true", "python3 main.py $IP $PORT $DURATION $PACKET_SIZE $THREADS" ] }
          - step: { name: Runner 29, image: python:3.10, script: [ "chmod +x mustafa || true", "python3 main.py $IP $PORT $DURATION $PACKET_SIZE $THREADS" ] }
          - step: { name: Runner 30, image: python:3.10, script: [ "chmod +x mustafa || true", "python3 main.py $IP $PORT $DURATION $PACKET_SIZE $THREADS" ] }
