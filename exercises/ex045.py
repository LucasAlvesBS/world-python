from colorama import Fore, init
from random import randint

init(autoreset=True)

cyan = Fore.CYAN
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
magenta = Fore.MAGENTA

separator = magenta + '-=-' * 25

print(separator)
print(cyan + (' ' * 30 + 'JOKENPÔ'))
print(separator)

print(cyan + '(1) Pedra \n(2) Papel \n(3) Tesoura')
print(separator)
print(cyan + 'Escolha o número do símbolo correspondente e tente vencer a máquina!')
print(separator)

user = int(input('Número do símbolo: '))
pc = randint(1, 3)

if user < 1 or user > 3:
    print('Este não é um símbolo válido. Tente novamente!')
else:
    stone = 'Pedra'
    paper = 'Papel'
    scissors = 'Tesoura'

    if pc == 1:
        pc_symbol = stone
    elif pc == 2:
        pc_symbol = paper
    else:
        pc_symbol = scissors

    if user == 1:
        user_symbol = stone
    elif user == 2:
        user_symbol = paper
    else:
        user_symbol = scissors

    print(separator)
    print(f'Escolha da máquina: {pc_symbol}')
    print(f'Escolha do usuário: {user_symbol}')

    victory_message = green + 'GANHOU! Você é muito bom nesse jogo!'
    defeat_message = red + 'VOCÊ PERDEU! HAHAHAHAHAHA'
    draw_message = yellow + 'Empate! Vamos jogar novamente!'

    if pc == 1 and user == 3:
        print(defeat_message)
    elif pc == 1 and user == 2:
        print(victory_message)
    elif pc == 2 and user == 1:
        print(defeat_message)
    elif pc == 2 and user == 3:
        print(victory_message)
    elif pc == 3 and user == 1:
        print(victory_message)
    elif pc == 3 and user == 2:
        print(defeat_message)
    else:
        print(draw_message)