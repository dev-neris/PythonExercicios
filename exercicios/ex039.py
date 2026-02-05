from datetime import date
nasc = int(input('Ano de nascimento:'))
atual = date.today().year
idade = atual - nasc

print(f'Quem nasceu em {nasc} tem {idade} anos')

if idade == 18:
    print('Você precisa se alistar IMEDIATAMENTE!')

elif idade < 18:
    print('Ainda não está no momento de você se alistar.')
    saldo = 18 - idade
    print(f'Faltam {saldo} anos para você se alistar.')
    ano = atual + saldo
    print(f'O ano do seu alistamento será em {ano}')

elif idade > 18:
    print('Seu alistamento já passou.')
    saldo = idade - 18
    print(f'Seu alistamento foi há {saldo} anos')
    ano = atual - saldo
    print(f'O ano do seu alistamento foi em {ano}')