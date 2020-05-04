import os
import socket
import time

HOST = '0.0.0.0'
PORT = 60002

def TaskList(conn):
    print('[+] Sending task list...')
    os.system('tasklist > tasklist.txt')
    with open('tasklist.txt', 'rb') as f:
        taskList = f.read()
    os.system('del tasklist.txt')
    data_length = len(taskList)
    conn.send(data_length.to_bytes(4, 'big'))
    conn.send(taskList)
    print("[+] Done")

def TaskKill(conn):
    k = conn.recv(1024)
    k = k.decode()
    print(f'[+] Killing task \"{k}\"...')
    os.system(f"taskkill /F /IM {k}")
    print('[+] Done')

while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            print("[+] Connected to ", addr)
            while True:
                m = conn.recv(1024).decode()
                if m=='tasklist':
                    TaskList(conn)
                    TaskKill(conn)
                if m=='lock':
                    os.system('rundll32.exe user32.dll,LockWorkStation')
                    break
                if m=='found':
                    break
                if m=='exit':
                    break
        print("[+] Disconnected")
    except:
        pass
