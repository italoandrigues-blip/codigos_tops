import time 
import os
from rich.console import Console

console = Console()

#clr limpa no windows e clear linux/mac
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def write(text, speed, color):
    Linha = ""

    for Letra in text:
        Linha += Letra
        console.print(f"[{color}]{Linha}[/]", end="\r")
        time.sleep(speed)

    console.print(f"[bold {color}]{text}[/]")
    time.sleep(1)

#fiz essa funçao so pra deixar o codigo bonito
def musga():
    write("ola eu me chamo italo", 0.05, "red")
    console.print()
    write("to testando o codigo top", 0.05, "blue")

musga()

clear()