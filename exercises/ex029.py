from colorama import Fore, init

init(autoreset=True)

speed = int(input('Digite a velocidade do carro em km/h: '))
limit = 80
fine = 7

if speed > limit:
    totalToPay = (speed - limit) * fine
    print(Fore.RED + f'\nMULTADO! Você excedeu o limite de velocidade permitido que é de 80km/h')
    print(Fore.RED + 'Você deve pagar uma multa de ' + Fore.YELLOW + f'R${totalToPay:.2f}!')

print(Fore.GREEN + '\nTenha um bom dia! Dirija com segurança!')