#Deposito, saque e extrato

menu = """Bem Vindo ao Banco
Escolha uma opção
[1]Deposito
[2]Saque
[3]Extrato
[0]Sair

"""

saldo = 0.0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
	opcao = int(input(menu))

	if opcao == 0:
		break
	elif opcao == 1:
		valor = float(input("Digite o valor que deseja depositar: R$ "))
		extrato += f"Deposito no valor de R$ {valor:.2f}\n"
		saldo += valor
	elif opcao == 2:
		if numero_saques < LIMITE_SAQUES:
			valor = float(input("Digite o valor que deseja sacar: R$ "))
			if saldo >= valor and valor <= 500:
				extrato += f"Saque no valor de R$ {valor:.2f}\n"
				numero_saques += 1
				print("Saque Relizado com Sucesso")
			else:
				print("Saldo insuficiente ou valor desejado maior que 500")
		else:
			print("Número de saques diarios excedidos")
	elif opcao == 3:
		print(extrato)
else:
	print("Digite uma opção válida\n")






