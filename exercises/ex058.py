from random import randint

equalSeparator = '=' * 40
hyphenSeparator = '-' * 40

print(equalSeparator)
print(' ' * 15 + 'ADVINHAÇÃO')
print(equalSeparator)

pcNum = 15
playerNum = 20
count = 0

pcNum = randint(0, 10)

while playerNum != pcNum:
  playerNum = int(input('Digite um número de 0 a 10: '))
  count += 1
  
  if (playerNum < pcNum):
    print('\nMais... Tente novamente!')
    print(hyphenSeparator)
  elif (playerNum > pcNum):
    print('\nMenos... Tente novamente!')
    print(hyphenSeparator)
  
print(f'\nPARABÉNS! Depois de {count} tentativa(s), você advinhou o número escolhido pelo PC.')
