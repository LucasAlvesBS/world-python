num = input('Digite um número de 0 a 9999: ').zfill(4)

unidade = num[3]
dezena = num[2]
centena = num[1]
milhar = num[0]

print(f'\nUnidade: {unidade}\nDezena: {dezena}\nCentena: {centena}\nMilhar: {milhar}')