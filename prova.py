par = 0
impar = 0
#pede 10 numeros no terminal
for i in range(10):
    n = int(input("numero :"))
    #verifica se o numero é par ou impar e soma os pares e os impares
    if n % 2 == 0:
         par = par + n
    else:
         impar = impar + n

print (f"a soma dos pares é {par}")
print (f"a soma dos impares é: {impar}")