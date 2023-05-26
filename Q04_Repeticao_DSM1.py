#Questão 04 da Lista de Repetição no Python Brasil
#https://wiki.python.org.br/EstruturaDeRepeticao 

#Configurações iniciais para validação das entradas
popA = 1
popB = 0
txA = 0
txB = 1
#Validação: só sai do laço while quando a popA < popB e txA > txB
while True:
    if popA >= popB:
        popA = float(input("PopA: "))
        popB = float(input("PopB: "))

    if txA <= txB:
        txA = float(input("txA: "))
        txB = float(input("txB: "))

    #Se as entradas estão OK, sai do laço while
    if popA < popB and txA > txB:
        break

anos = 0
while popA < popB:
    #Crescimento das populações de acordo com as taxas
    popA += popA*(txA/100)
    popB += popB*(txB/100)
    anos += 1 #passou-se mais um ano

print("popA:", popA)
print("popB:", popB)
print("e foi preciso de:", anos, " anos!")