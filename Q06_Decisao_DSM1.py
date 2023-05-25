#Questão 06 da Lista de Comandos de Decisão no Python Brasil
#https://wiki.python.org.br/EstruturaDeDecisao 

x = float( input("x: ") )
y = float( input("y: ") )
z = float( input("z: ") )

if x == y and x == z:
    print("São todos iguais!")
elif x > y and x > z:
    print("O maior deles é o", x)
elif y > z:
    print("O maior deles é o", y)    
else:
    print("O maior deles é o", z)





