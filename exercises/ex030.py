from colorama import Fore, init

init(autoreset=True)

num = int(input(Fore.MAGENTA + 'Me diga um número inteiro qualquer: '))
rest = num % 2

standardSentence = f'O número {num} é ' + Fore.BLUE

if rest == 0:
    print(standardSentence + 'PAR')
else:
    print(standardSentence + 'IMPAR')