from random import randint
from colorama import Fore, init
from time import sleep

init(autoreset=True)
separator = '-=-' * 50

print(Fore.YELLOW + separator)
print(Fore.BLUE + 'Vou pensar em um número entre 0 e 5. Tente advinhar... ')
print(Fore.YELLOW + separator)

pcNum = randint(0, 5)
userNum = int(input('Em que número eu pensei? '))

print(Fore.MAGENTA + 'PROCESSANDO...')
sleep(2)

if pcNum == userNum:
    print(Fore.GREEN + 'PARABÉNS! Você conseguiu me vencer!')
else:
    print(Fore.RED + f'GANHEI! Eu pensei no número {pcNum} e não no {userNum}!')