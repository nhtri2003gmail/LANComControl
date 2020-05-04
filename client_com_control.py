import os
import socket
import time

PORT = 60002

gateWay = input('Enter default gateway: ')
t = gateWay.split('.')
partGate = str(t[0]) + '.' + str(t[1]) + '.' + str(t[2]) + '.'
for i in range(0, 256):
    HOST = partGate + str(i)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.settimeout(0.1)
            s.connect((HOST, PORT))
            s.sendall(b"found")
        except:
            print(HOST + ': False')
        else:
            print(f"[+] Found server ip: {HOST}")
            s.close()
            break
    

def TaskList(s):
    remaining = int.from_bytes(s.recv(4), 'big')
    taskList = b''
    while remaining:
        t = s.recv(min(remaining, 4096))
        remaining -= len(t)
        taskList+=t
    print(taskList.decode())
    print("Enter the full name of the task you want to kill")
    while True:
        k = input('> ')
        if not k=='':
            break
    s.send(k.encode())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print('[+] Connecting to server...')
    time.sleep(1)
    s.connect(('192.168.10.118', PORT))
    print('[+] Connected successfully')
    while True:
        print()
        print("Choose the number: ")
        print("1. Tasklist")
        print("2. Lock")
        print('3. Exit server')
        c = input("Your choice > ")
        if c=='1':
            s.sendall('tasklist'.encode())
            TaskList(s)
        if c=='2':
            s.sendall('lock'.encode())
            break
        if c=='3':
            s.sendall('exit'.encode())
            break
        os.system('cls')
