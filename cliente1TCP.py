
"""
Desenvolvido por: Jose M.S.M. Neto 27/05 para a disciplina de Redes de Computadores II
Universidade Federal do Para
"""

import socket
import threading
import time
import os
import sys
negrito, white, yellow, magenta, fim, ciano = "\033[1m", "\033[37m", "\033[33m", "\033[35m", "\033[0;0m", "\033[36m"	
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def animation(k, phrase):	
	if k == 0:
		print("\033[K" , negrito + white + phrase + fim + negrito + yellow + "               " , end = "\r")
	elif k == 1:
		print("\033[K" , negrito + white + phrase + fim + negrito + yellow + " #             " , end = "\r")
	elif k == 2:
		print("\033[K" , negrito + white + phrase + fim + negrito + yellow + " # #           " , end = "\r")
	elif k == 3:
		print("\033[K" , negrito + white + phrase + fim + negrito + yellow + " # # #         " , end = "\r")
	elif k == 4:
		print("\033[K" , negrito + white + phrase + fim + negrito + yellow + " # # # #       " , end = "\r")
	elif k == 5:
		print("\033[K" , negrito + white + phrase + fim + negrito + yellow + " # # # # #     " , end = "\r")
	elif k == 6:
		print("\033[K" , negrito + white + phrase + fim + negrito + yellow + " # # # # # #   " , end = "\r")
	else:
		print("\033[K" , negrito + white + phrase + fim + negrito + yellow + " # # # # # # # " , end = "\r")

def file1():
	name = "TODO_MUNDO_ODEIA_O-CHRIS-TODO_MUNDO_ODEIA_SER-ROUBADO_T02E05.mp4"	
	path = os.getcwd() + "/todo_mundo_odeia_o_chris.mp4"
	u = 0
	while True:
		arq = open(path, 'ab')
		print("\033[K" , negrito + white + " [*] Downloading file " + fim + negrito + ciano + name + " " + str(u) + fim, end = "\r")
		data = client.recv(1024)
		if bytes("/!ENDFILE/", "utf-8") in data:
			arq.write(data)
			arq.close()
			break
		elif data == bytes("/!ENDFILE/", "utf-8"):
			arq.close()
			break
		else:
			arq.write(data)
			arq.close()
		u+=1
	print(negrito + white + "File successfully downloaded" + fim)
def file2():
	name = "SPONGEBOB_TRAP_REMIX.mp3"	
	path = os.getcwd() + "/sponge_bob_remix.mp3"
	u = 0
	while True:
		arq = open(path, 'ab')
		print("\033[K" , negrito + white + " [*] Downloading file " + fim + negrito + ciano + name + " " + str(u) + fim, end = "\r")
		data = client.recv(1024)
		if bytes("/!ENDFILE/", "utf-8") in data:
			arq.write(data)
			arq.close()
			break
		elif data == bytes("/!ENDFILE/", "utf-8"):
			arq.close()
			break
		else:
			arq.write(data)
			arq.close()
		u+=1
	print(negrito + white + "File successfully downloaded" + fim)
def file3():
	name = "REDES2.pdf"	
	path = os.getcwd() + "/redes2.pdf"
	u = 0
	while True:
		arq = open(path, 'ab')
		print("\033[K" , negrito + white + " [*] Downloading file " + fim + negrito + ciano + name + " " + str(u) + fim, end = "\r")
		data = client.recv(1024)
		if bytes("/!ENDFILE/", "utf-8") in data:
			arq.write(data)
			arq.close()
			break
		elif data == bytes("/!ENDFILE/", "utf-8"):
			arq.close()
			break
		else:
			arq.write(data)
			arq.close()
		u+=1
	print(negrito + white + "File successfully downloaded" + fim)
	print("")

def download():
		menu =  "\n" + negrito + yellow + "          NETO`s SERVER WITH TCP RENUE        " + fim + "\n"
		menu += negrito + white + "			 ____________________________" + fim + "\n"
		menu += negrito + white + "			|   Computer Networks II     |" + fim + "\n"
		menu += negrito + white + "			| Federal University of Para |" + fim + "\n"
		menu += negrito + white + "			|____________________________|" + fim + "\n\n"
		menu += negrito + ciano + "A) " + fim + negrito + white + "TODO_MUNDO_ODEIA_O-CHRIS-TODO_MUNDO_ODEIA_SER-ROUBADO_T02E05.mp4" + fim + "\n"
		menu += negrito + ciano + "B) " + fim + negrito + white + "SPONGEBOB_TRAP_REMIX.mp3  "+ fim + "\n"
		menu += negrito + ciano + "C) " + fim + negrito + white + "REDES2.pdf"+ fim + "\n"
		menu += negrito + ciano + "D) " + fim + negrito + white + "EXIT "+ fim + "\n"
		print(menu)
		try:
			dec = (input(negrito + yellow + "         choose? \n"  + fim)).upper()
			while dec != "A" and dec != "B" and dec != "C" and dec != "C" and dec != "D":
				dec = (input(negrito + yellow + "         choose (only A,B,C or D) \n"  + fim)).upper()
			if dec == "A":
				client.send(bytes("/!decA!/", "utf-8"))
				file1()
			elif dec == "B":
				client.send(bytes("/!decB!/", "utf-8"))
				file2()
			elif dec == "C":
				client.send(bytes("/!decC!/", "utf-8"))
				file3()
			else:
				client.close()
				sys.exit(0)
		except (KeyboardInterrupt):
			print("")
			sys.exit(0)

def connection_server():
	k = 0	
	while True:
		try:		
			con = " [*] Trying connection "
			animation(k, con)
			if k == 7:
				k = 0
			else:
				k += 1
			client.connect((target_host, target_port))
			print(negrito + white + "[*] Successful connection > Server " + fim + negrito + magenta + target_host + ":" + str(target_port) + fim)
			break
		except:		
			pass
	download()

target_host = input(negrito + white + "[*] Server: " + fim)
target_port = int(input(negrito + white + "[*] Port: " + fim))
connection_server()

