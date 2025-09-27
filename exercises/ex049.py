multiplicationTable = int(input('Digite um número para saber a tabuada: '))

separator = '-' * 20
print(separator)

for number in range(1, 11):
    print(f'{multiplicationTable} x {number} = {multiplicationTable * number}')

print(separator)