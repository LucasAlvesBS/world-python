name = input('Digite o nome completo: ')

split = name.split()

firstName = split[0]
lastName = split[-1]

print(f'\nPrimeiro nome: {firstName}\nÚltimo nome: {lastName}')