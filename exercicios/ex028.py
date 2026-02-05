from random import randint
from time import sleep
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. tente adivinhar...')
print('-=-' * 20)
n = int(input('Em que número eu pensei?'))
print('PROCESSANDO...')
sleep(2)
aleatorio = randint(0,5)
if n == aleatorio:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(aleatorio, n))

