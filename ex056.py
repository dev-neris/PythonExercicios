soma = 0
maior = 0
cont = 0
nomevelho = ''
for c in range(1,5):
    print(f'----- {c}ª PESSOA ------')
    nome = str(input('Nome:')).upper().strip()
    idade = int (input('Idade:'))
    soma += idade / 4
    sexo = str(input('Sexo [M/F]:')).upper().strip()
    if c == 1 and sexo == 'M':
        maior = idade
        nomevelho = nome
    if sexo == 'M' and idade > maior:
        maior = idade
        nomevelho = nome

    if idade < 20 and sexo == 'F':
       cont += 1

print(f'A média de idade do grupo é de {soma} anos')
print(f'O homem mais velho tem {maior} anos e se chama {nomevelho}.')
print(f'Ao todo são {cont} mulheres com menos de 20 anos.')