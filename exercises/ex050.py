num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
num3 = int(input('Terceiro número: '))
num4 = int(input('Quarto número: '))
num5 = int(input('Quinto número: '))
num6 = int(input('Sexto número: '))

sum = 0
numbers = [num1, num2, num3, num4, num5, num6]

print('\nValores considerados:')

for number in numbers:
    if number % 2 == 0:
        print(number)
        sum += number

print(f'\nA soma dos números pares equivale a {sum}')
