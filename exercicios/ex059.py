from time import sleep
n1 = int(input('Primeiro valor'))
n2 = int(input('Segundo valor:'))
opcao = 0

while opcao != 5:
    print('''[ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('>>>>> Qual é a sua opção?'))
    if opcao == 1:
        print(f'A soma entre {n1} + {n2} é {n1+n2}')
    elif opcao == 2:
        print(f'O resultado de {n1} x {n2} é {n1*n2}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'O maior número entre {n1} e {n2} é {maior}')
    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor:'))
        n2 = int(input('Segundo valor:'))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
sleep(2)
print('Fim do programa! Volte sempre!')