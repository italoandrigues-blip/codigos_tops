#sistema bancario
import os
import time

def limpar():
    os.system("cls")

saldo = 1000

while True:

    opcoes = input('O que deseja?\n'
    '1- Ver saldo;\n'
    '2- Sacar dinheiro;\n' 
    '3- Transferir dinheiro;\n'
    '4- Depositar dinheiro;\n'
    '5- Fechar tudo;\n')

    if opcoes == '1':
        print(f'Seu saldo é de R${saldo}')

    elif opcoes == "2":
        saque = float(input("Quanto deseja sacar? "))
        if saque > saldo:
            print("Saldo Insuficiente")
        else: 
            saldo = saldo - saque
            print(f"Saldo restante: {saldo}")

    elif opcoes == "3":
        transfer = float(input("Quanto deseja tranferir?"))
        transfer2 = input("Para quem deseja fazer a transferencia?\n ")
        if transfer > saldo:
            print("saldo insuficiente! ")
        else:
            saldo -= transfer
            print(f"Voce transferiu R${transfer} para a conta de {transfer2}\n\nSeu saldo atual é de R${saldo}")
            
        

    elif opcoes == "5":
        print("finalizando operacao... ")
        break

    elif opcoes == "4":
        deposito = int(input("Quanto deseja depositar? "))
        saldo += deposito
        print(f"Voce depositou {deposito}.\nSeu saldo atual é de R${saldo}")

    time.sleep(2)