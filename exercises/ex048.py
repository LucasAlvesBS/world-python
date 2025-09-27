print('Os números impares, múltiplos de 3, entre 1 e 500 são:\n')

for number in range(1, 500):
    if number % 2 == 1 and number % 3 == 0:
        print(number)