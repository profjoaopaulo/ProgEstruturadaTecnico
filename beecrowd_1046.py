#https://www.beecrowd.com.br/judge/pt/problems/view/1046

entrada = input()
inicio, termino = entrada.split()
inicio = int(inicio)
termino = int(termino)

#Se o inicio do jogo for maior ou igual ao término, significa que foi de um dia pro outro
if inicio >= termino:
    print("O JOGO DUROU %i HORA(S)" % (termino+24-inicio))
else:
    print("O JOGO DUROU %i HORA(S)" % (termino-inicio))