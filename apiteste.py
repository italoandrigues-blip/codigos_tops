import requests
from rich.console import Console

console = Console()

resposta = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL").json()

valor_compra = resposta['USDBRL']['bid']
valor_venda = resposta['USDBRL']['ask']

print("=" * 40)
pergunta = console.input("   O QUE DESEJA FAZER?\n" 
"1 - Ver valor de compra do dolar\n" 
"2 - Ver valor de venda do dolar\n")
if pergunta == "1":
    print(f'O valor de compra do dolar é: {valor_compra}')
elif pergunta == "2":
    print(f'O valor de venda do dolar é {valor_venda}')
else:
    print("Resposta invalida")