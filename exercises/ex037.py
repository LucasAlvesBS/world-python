from colorama import Fore, init

init(autoreset=True)

separator = '-=-' * 20
magenta = Fore.MAGENTA
cyan = Fore.CYAN
red = Fore.RED

num = int(input(cyan + 'Digite o número inteiro: '))
print(separator)
print(magenta + '(1) Binário \n(2) Octal \n(3) Hexadecimal')
print(separator)
base = int(input(cyan + 'Escolha o número que se refere a base de conversão: '))

if base == 1:
    convertedValue = bin(num)[2:]
    baseName = 'binário'
    print(magenta + f'A base escolhida foi {baseName} e o seu valor convertido é de {convertedValue}.')
elif base == 2:
    convertedValue = oct(num)[2:]
    baseName = 'octal'
    print(magenta + f'A base escolhida foi {baseName} e o seu valor convertido é de {convertedValue}.')
elif base == 3:
    if num < 0:
        convertedValue = hex(num)[3:]
    else:
        convertedValue = hex(num)[2:]
    baseName = 'hexadecimal'
    print(magenta + f'A base escolhida foi {baseName} e o seu valor convertido é de {convertedValue}.')
else:
    print(red + 'Base de conversão inválida. Tente novamente!')

