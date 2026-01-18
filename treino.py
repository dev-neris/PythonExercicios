peso = float(input('Qual o peso das toneladas?'))
preco_por_tonelada = float(input('Qual o preço por tonelada?'))
print('''| NOVO CLIENTE
| CLIENTE FIDELIZADO
| CLIENTE PREMIUM''')
tipo_cliente = str(input('Qual é a sua categoria?')).upper().strip()

valor_total = peso * preco_por_tonelada

if tipo_cliente == 'NOVO CLIENTE':
    valor_final = valor_total
    print(f'O valor ficará R${valor_final:.2f}')

elif tipo_cliente == 'CLIENTE FIDELIZADO':
    valor_final = valor_total - (valor_total * 5 / 100)
    print(f'Seu desconto será de R${valor_final:.2f}')

elif tipo_cliente == 'CLIENTE PREMIUM':
    valor_final = valor_total - (valor_total * 10 / 100)
    print(f'No total seu desconto será de R${valor_final:.2f}')

else:
    print('OPÇÃO INVÁLIDA')

