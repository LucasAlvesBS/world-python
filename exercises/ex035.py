separator = '-=' * 20

print(separator)
print('Analisador de Triângulos')
print(separator)

straight1 = float(input('Digite o valor da primeira reta: '))
straight2 = float(input('Digite o valor da segunda reta: '))
straight3 = float(input('Digite o valor da terceira reta: '))

if (straight1 + straight2 > straight3) and (straight2 + straight3 > straight1) and (straight1 + straight3 > straight2):
    print(f'\nAs retas {straight1}, {straight2} e {straight3} PODEM formar um triângulo.')
else:
    print(f'\nAs retas {straight1}, {straight2} e {straight3} NÃO PODEM formar um triângulo.')