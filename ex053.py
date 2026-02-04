frase = str(input('Digite uma frase:')).upper().strip()
divisao = frase.split()
junto = ''.join(divisao)
inverso = ''
for letra in range (len(junto) -1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
  print('Temos um palíndromo!')
else:
  print('A frase digitida não é um palíndromo!')
