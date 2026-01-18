from datetime import date
nasc = int(input('Ano de nascimento:'))
atual = date.today().year
idade = atual - nasc

print(f'Quem nasceu em {nasc} tem {idade}')

if idade == 18:
    print('Você precisa se alistar IMEDIATAMENTE!')

elif idade < 18:
    print('Seu alistamento ainda vai ocorrer.')
    saldo = 18 - idade
    print(f'Faltam {saldo} anos para você se alistar.')
    ano = atual + saldo
    print(f'Seu alistamento será em {ano}')

elif idade > 18:
    print('Seu alistamento já passou.')
    saldo = idade - 18
    print(f'Seu alistamento foi há {saldo} anos')
    ano = atual - saldo
    print(f'Seu alistamento foi em {ano}')