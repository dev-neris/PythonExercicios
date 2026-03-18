c = 1
while True:
    num = int(input('Quer ver a tabuada de qual valor?'))
    if num < 0:
        break
    print('_' * 30)
    while c <= 10:
        print(f'{num} x {c} = {num*c}')

        c += 1
