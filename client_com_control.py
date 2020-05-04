import os
import socket

HOST = input('Enter server ip address: ')
##HOST = '127.0.0.1'
PORT = 60002

def TaskList(s):
    remaining = int.from_bytes(s.recv(4), 'big')
    taskList = b''
    while remaining:
        t = s.recv(min(remaining, 4096))
        remaining -= len(t)
        taskList+=t
    print(taskList.decode())
    print("Enter the full name of the task you want to kill")
    k = input('> ')
    s.send(k.encode())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Choose the number: ")
    print()
    print("1. Tasklist")
    print("2. Lock")
    while True:
        c = input("Your choice > ")
        if c=='1':
            s.sendall('tasklist'.encode())
            TaskList(s)
            break
        if c=='2':
            s.sendall('lock'.encode())
            break
