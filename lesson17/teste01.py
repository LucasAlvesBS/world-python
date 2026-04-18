num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)

if 5 in num:
  num.remove(5)
else:
  print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elements.')

separator = '-' * 40

print(separator)

values = list()

for count in range(0, 2):
  values.append(int(input('Digite um valor: ')))

for index, value in enumerate(values):
  print(f'Na posição {index} encontrei o valor {value}!')
print('Cheguei ao final da lista.')

print(separator)

a = [2, 3, 4, 7]
# ligação entre a e b, por isso ao alterar uma lista, afeta a outra
b = a
# apenas a cópia de a em c, ou seja, listas diferentes
c = a[:]
b[2] = 8
c[3] = 1
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'Lista C: {c}')
