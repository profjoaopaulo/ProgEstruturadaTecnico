#Questão 1018 do beecrowd
#https://www.beecrowd.com.br/judge/pt/problems/view/1018 (Cédulas)

#Entrada
valor = int( input() )

print(valor) #É pedido para imprimir o valor lido

#Decomposição em notas
n100 = valor // 100
valor = valor - n100*100
n50 = valor // 50
valor = valor - n50*50
n20 = valor // 20
valor = valor - n20*20
n10 = valor // 10
valor = valor - n10*10
n5 = valor // 5
valor = valor - n5*5
n2 = valor // 2
valor = valor - n2*2

#Saída conforme o exemplo do beecrowd
print("%d nota(s) de R$ 100,00" % n100)
print("%d nota(s) de R$ 50,00" % n50)
print("%d nota(s) de R$ 20,00" % n20)
print("%d nota(s) de R$ 10,00" % n10)
print("%d nota(s) de R$ 5,00" % n5)
print("%d nota(s) de R$ 2,00" % n2)
print("%d nota(s) de R$ 1,00" % valor)
