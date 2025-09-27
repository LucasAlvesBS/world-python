prime_number = int(input('Digite um número: '))

accumulated = 0

for value in range(1, prime_number + 1):
    if prime_number % value == 0:
        accumulated += 1

print(f'\nO número {prime_number}', end=' ')

if accumulated == 2:
    print('é PRIMO!')
else:
    print('NÃO é primo!')