from colorama import Fore, init

init(autoreset=True)

prime_number = int(input('Digite um número: '))

accumulated = 0

yellow = Fore.YELLOW
red = Fore.RED

for value in range(1, prime_number + 1):  
    color = red 
    if prime_number % value == 0:
        color = yellow
        accumulated += 1
    print(color + str(value), end=' ')

print(f'\nO número {prime_number} foi dividido {accumulated} vez(es) e, por isso,', end=' ')

if accumulated == 2:
    print('é PRIMO!')
else:
    print('NÃO é primo!')