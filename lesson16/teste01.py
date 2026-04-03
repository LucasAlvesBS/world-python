foods = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(foods[:2])

for food in foods:
  print(f'Vou comer {food}')
print('Comi muito!')

separator = '-' * 20

print(separator)

for count in range(0, len(foods)):
  print(foods[count])
  
print(separator)

for index, food in enumerate(foods):
  print(f'{food} na posição {index}')

print(separator)

print(sorted(foods))

print(separator)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(len(c))
print(c.count(5))
print(c.index(8))
print(c.index(2, 1))

print(separator)

person = ('Gustavo', 39, 'M', 99.88)
print(person)

# Não é possível deletar apenas um item da tupla, mas a tupla inteira pode ser deletada com o del
del(person)



