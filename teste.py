soma = 0
n = 1
while n <= 4:
    num = int(input('Digite a nota: '))
    soma += num
    n += 1
media = soma / 4

if media >= 7:
    print('Aprovado!')

elif media >= 5 and media < 7:
    print('Recuperação')

else:
    print('Reprovado')
print('A média sera de ', media)