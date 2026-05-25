import time
import os
from rich.console import Console

console = Console()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

n1 = int(input("Digite um numero: "))
time.sleep(0.3)
n2 = int(input("Digite o segundo numero: "))

operacao = input("Qual operador? ")

if operacao =="*":
    print(f"A resposta é: {n1 *  n2}")
    console.print()

elif operacao == "+":
    print(f"A resposta é: {n1 +  n2}")
    console.print()

elif operacao == "-":
    print(f"A resposta é: {n1 -  n2}")
    console.print()

elif operacao == "/":
    print(f"A resposta é: {n1 /  n2}")
    console.print()

time.sleep(1)
contagem = 5

while contagem >= 0:
    print(f"Calculadora encerrando em: {contagem}")
    time.sleep(1)
    contagem = (contagem - 1)


clear()