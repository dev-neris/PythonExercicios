from random import randint
v = 0
print('-=' * 30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 30)

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    parimpar = ' '
    while parimpar not in 'PI':
        parimpar = str(input('Par ou Ímpar? [P/I]')).strip().upper()
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')

    if parimpar == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif parimpar == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break

    print('Vamos jogar novamente...')

print(f'GAME OVER! Você venceu {v} vezes.')

