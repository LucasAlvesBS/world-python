separator = '-=' * 20

print(separator)
print(' ' * 9 + 'PROGRESSÃO ARITMÉTICA')
print(separator)

term = int(input('Digite o valor primeiro termo: '))
reason = int(input('Digite o valor da razão: '))
print(end='\n')

termLimit = 10
termCounting = 1
userResponse = ''

list_of_terms = [str(term)]

while userResponse != 'F':
  term += reason
  termCounting += 1
  list_of_terms.append(str(term))
  
  if (termCounting == termLimit):
    print('-> ' + ' '.join(list_of_terms))
    userResponse = str(input('\nDeseja continuar? [S/F] ')).strip().upper()
    
    if (userResponse == 'S'):
      incrementalTermLimit = int(input('Gostaria de ver mais quantos termos? '))
      termLimit += incrementalTermLimit
      print(end='\n')
  
