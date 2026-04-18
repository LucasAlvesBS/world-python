listOfNumbers = []

while True:
  value = int(input('Digite um valor: '))
  
  count = listOfNumbers.count(value)
  
  if count == 0:
    listOfNumbers.append(value)
    print('Valor adicionado com sucesso...')
  else:
    print('Valor duplicado! Não vou adicionar...')
    
  userResponse = ' '
  
  while userResponse not in 'SN':
    userResponse = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
  
  if userResponse == 'N':
    break
  
print('-=-' * 15)

listOfNumbers.sort()
print(f'Você digitou os valores {listOfNumbers}')
   