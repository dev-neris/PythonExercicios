nome = str(input('Digite seu nome:')).upper().strip()
idade = int(input('Digite sua idade:'))
espaco = nome.replace(' ', '')
print('Seu nome em maiúsculas {}'.format(espaco.upper()))
print('Seu nome em minúsculas {}'.format(espaco.lower()))
print('Seu nome tem {} letras'.format(len(espaco)))
if idade > 17:
    print('Você é maior de idade')
else:
    print('Você é menor de idade:')