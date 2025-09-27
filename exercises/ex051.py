separator = '-=' * 20

print(separator)
print('PROGRESSÃO ARITMÉTICA')
print(separator)

firstTerm = int(input('Primeiro termo: '))
ratio = int(input('Razão: '))
generalTerm = firstTerm + (10 - 1) * ratio

print(separator)
print('Os primeiros dez números dessa progressão aritmética são:\n')

for number in range(firstTerm, generalTerm + 1, ratio):
    print(number)
