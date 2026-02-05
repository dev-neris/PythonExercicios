print(f'{" Lojas Guanabara ":=^40}')
preco = float(input('Preço das compras:'))
print('''FORMAS DE PAGAMENTO:
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opcao = int(input('Qual sua opção?'))
if opcao == 1:
    avista = preco - (preco * 10 / 100)
    print(f'Sua compra de {preco:.2f} vai custar {avista:.2f} no final.')

elif opcao == 2:
    avista = preco - (preco * 5 / 100)
    print(f'À vista no cartão, sua compra de {preco:.2f} será de {avista:.2f}')

elif opcao == 3:
    valor = preco / 2
    print(f'Sua compra de {preco:.2f} será parcelada em 2x de {valor:.2f}, sem juros.')

elif opcao == 4:
    parcelas = int(input('Quantas parcelas?'))
    juros = preco + (preco * 20 / 100)
    valor = juros / parcelas
    print(f'Sua compra será parcelada em {parcelas}x de {valor:.2f} COM JUROS \n Sua compra de {preco:.2f} vai custar R${juros:.2f} no final.')

else:
    valor = preco
    print('OPÇÃO INVÁLIDA. tente novamente.')
