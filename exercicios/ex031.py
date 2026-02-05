distancia = int(input('Qual é a distância da sua viagem?'))
print('Você está prestes a começar uma viagem de {:.1f}Km.'.format(distancia))

if distancia <= 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45
print('E o preço será da sua passagem será de R${:.2f}'.format(valor))



