num = largerNumber = total = count = 0
userResponse = ''

while userResponse != 'N':
  num = int(input('Digite um número inteiro: '))
  
  if count == 0 or num < smallerNumber:
    smallerNumber = num
  
  if (num > largerNumber):
    largerNumber = num

  total += num
  count += 1
  
  print('Número computado!')
  
  userResponse = 'A'
  
  while userResponse not in 'SN':
    userResponse = str(input('\nDeseja continuar? [S/N] ')).strip().upper()[0]
  
  print('-' * 50)
  
average = total / count

print(f'\nA média entre os {count} valores é {average:.2f}')
print(f'O maior valor foi {largerNumber}')
print(f'O menor valor foi {smallerNumber}')  