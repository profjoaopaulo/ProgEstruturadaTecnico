'''
Faça um programa em Python que leia uma String do usuário e retorne todas as posições
(índices) em que se encontram as vogais.
'''
x = input("Texto: ")

for i in range(len(x)):
    if x[i] == 'a' or x[i] == 'e' or x[i] == 'i' or x[i] == 'o' or x[i] == 'u':
        print(i, end=' ')

print()