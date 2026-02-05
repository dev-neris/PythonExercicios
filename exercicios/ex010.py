real = float(input('Quanto dinheiro você tem na carteira? R$'))

dolar = real / 3.27

print('Com r$ {:.2f} você pode comprar us${:.2f}'.format(real, dolar))