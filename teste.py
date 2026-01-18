from random import randint
from time import sleep

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

lista = ['Pedra', 'Papel', 'Tesoura']

jogador = int(input('Qual é a sua jogada?'))
if jogador > 2 or jogador < 0:
    print('OPÇÃO INVÁLIDA!')
    exit()
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('-=' * 11)
computador = randint(0,2)
print(f'Computador jogou {lista[computador]}')
print(f'Jogador jogou {lista[jogador]}')
print('-=' * 11)

if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')

elif computador == 1: #computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')

elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')