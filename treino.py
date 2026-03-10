cont = 1
soma = 0

while cont <= 10:
    n = int(input('Digite um número:'))
    if n % 2 == 0:
        soma += 1
    cont += 1

print(f'Você digitou {soma} números pares.')


