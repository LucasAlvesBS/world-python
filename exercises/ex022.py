name = str(input('Digite seu nome completo: '))

upper = name.upper()
lower = name.lower()
nameLength = len(name.replace(' ', ''))
firstNameLength = len(name.split()[0].replace(' ', ''))



print(f'Nome em letras maiúsculas: {upper}')
print(f'Nome em letras minúsculas: {lower}')
print(f'Quantidade de letras do nome completo sem considerar espaços: {nameLength}')
print(f'Quantidade de letras do primeiro nome: {firstNameLength}')

