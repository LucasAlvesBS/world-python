from random import randint

equalSeparator = '=' * 40
hyphenSeparator = '-' * 40

print(equalSeparator)
print(' ' * 15 + 'ADVINHAÇÃO')
print(equalSeparator)

pcNum = 15
playerNum = 20
count = 0

while playerNum != pcNum:
  pcNum = randint(0, 10)
  playerNum = int(input('Digite um número de 0 a 10: '))
  count += 1
  
  print(f'\nNúmero selecionado pelo PC: {pcNum}')
  print(f'Número selecionado pelo Jogador: {playerNum}')
  print(hyphenSeparator)
  
print(f'\nPARABÉNS! Depois de {count} tentativa(s), você advinhou o número escolhido pelo PC.')
