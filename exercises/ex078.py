numbers = []

for position in range(0, 5):
  numbers.append(int(input(f'Digite um valor para a Posição {position}: ')))

print('-=-' * 25)
print(f'Você digitou os valores {numbers}')

largestNumber = max(numbers)
smallestNumber = min(numbers)

listOfLargestNumbers = []
listOfSmallestNumbers = []

for index, number in enumerate(numbers):
  if largestNumber == number:
    listOfLargestNumbers.append(f'{index}...')
      
  if smallestNumber == number:
    listOfSmallestNumbers.append(f'{index}...')

print(f'O maior valor digitado foi {largestNumber} na(s) posição(ões) {' '.join(listOfLargestNumbers)}')
print(f'O menor valor digitado foi {smallestNumber} na(s) posição(ões) {' '.join(listOfSmallestNumbers)}')
