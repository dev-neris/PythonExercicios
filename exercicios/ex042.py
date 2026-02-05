print('-=-' * 20)
print('Analisador de triângulos')
print('-=-' * 20)
a = float(input('Primeiro segmento:'))
b = float(input('Segundo segmento:'))
c = float(input('Terceiro segmento:'))

if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acimas PODEM FORMAR triângulos')
    if a == b == c:
        print('EQUILÁTERO!')
    elif a != b != c != a:
        print('ESCALENO!')
    else:
     print('ISÓSCELES!')

else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')

