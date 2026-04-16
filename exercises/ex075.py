num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: ')) 
num3 = int(input('Digite mais um número: '))
num4 = int(input('Digite o último número: '))

print('-' * 50)

tupleOfNumbers = (num1, num2, num3, num4)
print(f'Você digitou os valores: {tupleOfNumbers}')

numberOfTimes9 = tupleOfNumbers.count(9)
print(f'O valor 9 apareceu {numberOfTimes9} vez(es)')

numberOfTimes3 = tupleOfNumbers.count(3)

position3 = 0

print(f'O valor 3', end = ' ')

if numberOfTimes3 != 0:
  position3 = tupleOfNumbers.index(3) + 1
  print(f'apareceu na {position3}ª posição')
else:
  print('não foi digitado em nenhuma posição')

countingEvenNumbers = 0

for tupleOfNumber in tupleOfNumbers:
  if tupleOfNumber % 2 == 0:
    countingEvenNumbers += 1
    
    if countingEvenNumbers == 1:
      print(f'O(s) valor(es) par(es) digitado(s) foi(foram)', end = ' ')
      
    print(tupleOfNumber, end = ' ')
    
if countingEvenNumbers == 0:
  print('Nenhum valor par foi digitado')
