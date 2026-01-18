dias = int(input('Quantos dias alugados?'))
km = float(input('Quantos Km rodados? '))
valor_total = (dias * 60) + (km * 0.15)
print('O Total a pagar é de R${:.2F}'.format(valor_total))

