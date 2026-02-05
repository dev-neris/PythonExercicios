print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)

pt = int(input('Primeiro Termo:'))
razao = int(input('Razão:'))

for c in range(1, 11):
    pa = pt + (c-1) * razao
    print(pa, end= ' ⮕ ')
print('ACABOU')