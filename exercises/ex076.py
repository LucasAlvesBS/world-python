separator = '-' * 30

print(separator)
print(' ' * 5 + 'LISTAGEM DE PREÇOS')
print(separator)

products = (
  'Lápis', 1.75, 
  'Borracha', 2, 
  'Caderno', 15.9, 
  'Estojo', 25, 
  'Transferidor', 4.2, 
  'Compasso', 9.99,
  'Mochila', 120.32,
  'Canetas', 22.3,
  'Livro', 34.9,
)

for index, product in enumerate(products):
  if index % 2 == 1:
    print(f'{product:6.2f}')
  
  if index % 2 == 0:
    print(f'{product:.<20}', end='R$ ')

print(separator)
