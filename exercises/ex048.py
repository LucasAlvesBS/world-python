print('Os números impares, múltiplos de 3, de 1 até 500 são:\n')

count = 0
sum = 0

for number in range(3, 501, 3):
    if number % 2 == 1:
        count += 1
        sum += number
        print(number, end=' ')

print(f'\n\nA quantidade números impares múltiplos de 3: {count}')        
print(f'A soma total desses números resultou em: {sum}')