valor = float(input('Valor da casa:'))
salario = float(input('Salário do comprador:'))
anos = int(input('Quantos anos de financiamento?'))

prestacao = valor / (anos*12)

print(f'Para pagar uma casa de R${valor:.2f} em {anos} anos a prestação mensal será de {prestacao:.2f}')

if prestacao <= (salario*30/100):
    print('Empréstimo concedido ')

else:
    print('Empréstimo negado')
