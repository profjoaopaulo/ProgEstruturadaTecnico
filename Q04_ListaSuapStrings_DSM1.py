'''
Faça um programa em Python que leia uma String do usuário e conte quantas palavras há na
mesma
'''
texto = input("Texto: ")
palavras = texto.split()
print(len(palavras))

