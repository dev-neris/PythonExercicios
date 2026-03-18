num = int(input('Digite um número:'))
primeiro = num
opcao = 'S'
soma = 0
maior = 0
menor = 0
c = 0
while opcao == 'S':
    soma += num
    c += 1
    if primeiro == num:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    opcao = str(input('Quer continuar? [S/N]')).upper().strip()
    if opcao == 'S':
        num = int(input('Digite um número:'))
media = soma / c

print(f'Você digitou {c} números e a média foi de {media:.2f} \n O maior valor digitado foi {maior} e o menor foi {menor}')

