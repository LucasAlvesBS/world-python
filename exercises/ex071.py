separator = '=' * 50

print(separator)
print(' ' * 20 + 'BANCO CEV')
print(separator)

count = 0

while True:
  currentValue = int(input('Que valor você quer sacar? R$'))
  
  if currentValue > 0:
    break

while True:
  if count == 0:
    bankNote = 50
  elif count == 1:
    bankNote = 20
  elif count == 2:
    bankNote = 10
  else:
    bankNote = 1
    
  amountOfBankNote = currentValue // bankNote
  totalValueAccordingToBankNote = amountOfBankNote * bankNote
  currentValue -= totalValueAccordingToBankNote
  
  if count == 0:
    print(end='\n')

  if amountOfBankNote > 0:
    print(f'Total de {amountOfBankNote} cédulas de R${bankNote:.2f}')
  
  if currentValue == 0:
    break
  
  count += 1
  
print(separator)
print('Volte sempre ao banco CEV! Tenha um bom dia!')