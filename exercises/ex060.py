num = int(input('Digite um número: '))

# Solução com WHILE
factorialWhile = num
resultWhile = 1

while factorialWhile != 1:
  resultWhile *= factorialWhile
  factorialWhile -= 1
  
print(f'\nResultado fatorial com WHILE: {resultWhile}')

# Solução com FOR
factorialFor = num
resultFor = 1

for c in range(num, 0, -1):
  resultFor *= factorialFor
  factorialFor -= 1
  
print(f'\nResultado fatorial com FOR: {resultFor}')