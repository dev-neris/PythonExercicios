soma = 0
cont = 0
for c in range (1, 501):
    if c % 2 == 1 and c % 3 == 0:
        soma += c
        cont += 1
print(f'A soma de todos os {cont} valores são {soma}')
