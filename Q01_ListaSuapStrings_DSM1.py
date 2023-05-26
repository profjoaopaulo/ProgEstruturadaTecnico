'''
Faça um programa em Python que leia uma String do usuário e retorne a mesma contendo todas
as vogais em letras maiúsculas.
'''
x = input("Texto: ")

for i in x:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        print(i.upper(), end='')
    else:
        print(i, end='')

print()