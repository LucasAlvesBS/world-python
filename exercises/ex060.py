from math import factorial

num = int(input('Digite um número: '))

# Solução com WHILE
factorialWhile = num
resultWhile = 1
 
print(f'{num}! = ', end='')

while factorialWhile > 0:
  print(f'{factorialWhile}', end='')
  print(' x ' if factorialWhile > 1 else ' = ', end='')
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

# Solução com MATH
resultMath = factorial(num)
print(f'\nResultado fatorial com MATH: {resultMath}')