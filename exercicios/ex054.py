from datetime import date

totmaior = 0
totmenor =  0
for c in range(1, 7+1):
    nasc = int(input(f'Em que ano a {c}ª pessoa nasceu?'))
    idade = date.today().year - nasc
    if idade >= 18:
        totmaior += 1
    elif idade < 18:
        totmenor += 1
print(f'Ao todo tivemos {totmaior} maiores de idade')
print(f'E também tivemos {totmenor} menores de idade')

