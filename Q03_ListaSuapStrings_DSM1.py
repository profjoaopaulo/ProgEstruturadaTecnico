'''
Faça um programa em Python que leia uma String do usuário que possa conter alguns números.
O programa deverá retornar a quantidade de números encontrados na String.
'''
x = input("Texto: ")
contadorNumeros = 0

for i in range(len(x)):
    if x[i].isnumeric():
        contadorNumeros += 1

print(contadorNumeros)
