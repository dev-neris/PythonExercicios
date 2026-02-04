frase = str(input('Digite uma frase:'))
divisao = frase.split()
junto = ''.join(divisao)
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')