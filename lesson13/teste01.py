i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

s = 0

for c in range(i, f + 1, p):
    print(c)
    s += c
print(f'\nO somatório de todos os valores foi {s}')