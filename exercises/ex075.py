num1 = int(input('Digite um número: '))

listOfEvenNumbers = []

if num1 % 2 == 0:
  listOfEvenNumbers.append(str(num1))

num2 = int(input('Digite outro número: '))

if num2 % 2 == 0:
 listOfEvenNumbers.append(str(num2))
  
num3 = int(input('Digite mais um número: '))

if num3 % 2 == 0:
  listOfEvenNumbers.append(str(num3))
  
num4 = int(input('Digite o último número: '))

if num4 % 2 == 0:
  listOfEvenNumbers.append(str(num4))

print('-' * 50)

tupleOfNumbers = (num1, num2, num3, num4)
print(f'Você digitou os valores: {tupleOfNumbers}')

numberOfTimes9 = tupleOfNumbers.count(9)
print(f'O valor 9 apareceu {numberOfTimes9} vez(es)')

numberOfTimes3 = tupleOfNumbers.count(3)

position3 = 0

print(f'O valor 3', end=' ')

if numberOfTimes3 != 0:
  position3 = tupleOfNumbers.index(3) + 1
  print(f'apareceu na {position3}ª posição')
else:
  print('não foi digitado em nenhuma posição')

if len(listOfEvenNumbers) > 0:
  print(f'O(s) valor(es) par(es) digitado(s) foi(foram) {' '.join(listOfEvenNumbers)}')
else:
  print('Nenhum valor par foi digitado')
