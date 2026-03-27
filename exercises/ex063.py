separator = '-=-' * 20

print(separator)
print(' ' * 17 + 'SEQUÊNCIA DE FIBONACCI')
print(separator)

numberOfTerms = int(input('Quantos termos da sequência de fibonacci gostaria de ver? '))

previousTerm = 0
currentTerm = 1
count = 0

print('\n0 1', end=' ')

while count != numberOfTerms:
  supportTerm = currentTerm
  currentTerm += previousTerm
  previousTerm = supportTerm 
  
  count += 1
  
  print(f'{currentTerm}', end=' ')
