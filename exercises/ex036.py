from colorama import Fore, init

init(autoreset=True)

separator = '-=-' * 20
yellow = Fore.YELLOW
red = Fore.RED
green = Fore.GREEN

print(separator)

homeValue = float(input(yellow + 'Informe o valor da casa: R$'))
buyerSalary = float(input(yellow + 'Informe o salário do comprador: R$'))
years = int(input(yellow + 'Informe em quantos anos ele pretende pagar: '))

print(separator)

salaryLimit = 30 / 100
months = years * 12
buyerMonthlyInstallmentLimit = buyerSalary * salaryLimit
requiredMonthlyInstallment = homeValue / months

if buyerMonthlyInstallmentLimit < requiredMonthlyInstallment:
    print(red + f'NEGADO! O comprador consegue pagar apenas a prestação mensal de ', end='')
    print(yellow + f'R${buyerMonthlyInstallmentLimit:.2f}')
    print(red + f'Porém, a prestação mensal necessária seria de ', end='')
    print(yellow + f'R${requiredMonthlyInstallment:.2f}')
else:
    print(green + f'MARAVILHA! O comprador consegue pagar a prestação mensal de R${requiredMonthlyInstallment:.2f}')
    print(green + 'Portanto, o empréstimo bancário será CONCEDIDO!')

