import os 
import subprocess
from wakeonlan import wol

'''177.220.18.'''

def printMenu():
	os.system('cls')
	print("---------------------")
	print("-----1-Ligado?    ---")
	print("-----2-Ligar      ---")
	print("-----Qualquer-Sair---")
	print("---------------------\n\n")

def pingPC(pcip):
	resultado = os.popen("ping -n 2 -w 500 " + pcip).read()

	if "TTL=" in resultado:
		return True

	return False

'''ends = {
	2: ("2c.44.fd.fa.fa.01", "177.220.18.44"),
	3: ("2c.44.fd.fa.ca.c2", "177.220.18.45"),
	4: ("2c.44.fd.fa.ea.dc", "177.220.18.46"),
	5: ("2c.44.fd.fa.fa.01", "177.220.18.47"),
	6: ("2c.44.fd.fa.fa.01", "177.220.18.48"),
	7: ("2c.44.fd.fa.fa.01", "177.220.18.49"),
	8: ("2c.44.fd.fa.fa.01", "177.220.18.50"),
	9: ("2c.44.fd.fa.fa.01", "177.220.18.51"),
	10: ("2c.44.fd.fa.fa.01", "177.220.18.52"),
	11: ("2c.44.fd.fa.fa.01", "177.220.18.53"),
	12: ("2c.44.fd.fa.fa.01", "177.220.18.54"),
	13: ("2c.44.fd.fa.fa.01", "177.220.18.55"),
	14: ("2c.44.fd.fa.fa.01", "177.220.18.56"),
	15: ("2c.44.fd.fa.fa.01", "177.220.18.57"),
	16: ("2c.44.fd.fa.fa.01", "177.220.18.58"),
	17: ("2c.44.fd.fa.fa.01", "177.220.18.59"),
	18: ("2c.44.fd.fa.fa.01", "177.220.18.60"),
	19: ("2c.44.fd.fa.fa.01", "177.220.18.61"),
	20: ("2c.44.fd.fa.fa.01", "177.220.18.62"),
	21: ("2c.44.fd.fa.fa.01", "177.220.18.63"),
	22: ("2c.44.fd.fa.fa.01", "177.220.18.64"),
	23: ("2c.44.fd.fa.fa.01", "177.220.18.65"),
	24: ("2c.44.fd.fa.fa.01", "177.220.18.66"),
	25: ("2c.44.fd.fa.fa.01", "177.220.18.67"),
	26: ("2c.44.fd.fa.fa.01", "177.220.18.68"),
	27: ("2c.44.fd.fa.fa.01", "177.220.18.69"),
	28: ("2c.44.fd.fa.fa.01", "177.220.18.70"),
	29: ("2c.44.fd.fa.fa.01", "177.220.18.71"),
	30: ("2c.44.fd.fa.fa.01", "177.220.18.72"),
	31: ("2c.44.fd.fa.fa.01", "177.220.18.73"),
	32: ("2c.44.fd.fa.fa.01", "177.220.18.74"),
	33: ("2c.44.fd.fa.fa.01", "177.220.18.76"),
	34: ("2c.44.fd.fa.fa.01", "177.220.18.77"),
	35: ("2c.44.fd.fa.fa.01", "177.220.18.78"),
	36: ("2c.44.fd.fa.fa.01", "177.220.18.79"),
	37: ("2c.44.fd.fa.fa.01", "177.220.18.80"),
	38: ("2c.44.fd.fa.fa.01", "177.220.18.81"),
	39: ("2c.44.fd.fa.fa.01", "177.220.18.82"),
}'''

while True:
	printMenu()

	try:
		try:
			op = int(input("Digite uma opção: "))
		except Exception as e:
			quit()

		if op == 1:
			os.system('cls')
			end = input("Digite o ip do PC: ")

			if pingPC(end):
				input("\n\n" + end + " - Ligado")
			else:
				input("\n\n" + end + " - Desligado")
		elif op == 2:
			os.system('cls')
			end = input("Digite o mac do PC: ")		

			wol.send_magic_packet(end)	

			os.system('cls')
			input('PC Ligado')
		else:
			quit()
	except Exception as e:
		os.system('cls')

		print(e)
		input("\n\nErro, saindo...")

		quit()
	
	
