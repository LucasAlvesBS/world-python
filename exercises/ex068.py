from random import randint

characterLimit = 20
macroSeparator = '=-' * characterLimit
microSeparator = '--' * characterLimit

print(macroSeparator)
print(' ' * 7 + 'VAMOS JOGAR PAR OU ÍMPAR')

victory = 0

while True:
  print(macroSeparator)
  num = int(input('Digite um valor: '))
  choice = ' '
  
  while choice not in 'PI':
    choice = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
  
  pc = randint(0, 10)
  result = num + pc
  
  print(microSeparator)
  print(f'Você jogou {num} e o computador {pc}, totalizando {result}.', end=' ')
  
  won = False

  if result % 2 == 0:
    print('DEU PAR!')
    
    if choice == 'P':
      won = True
      victory += 1
    
  if result % 2 == 1:
    print('DEU ÍMPAR!')
    
    if choice == 'I':
      won = True 
      victory += 1
      
  print(microSeparator)
    
  if won == False:
    print('Você PERDEU!')
    break
  
  print('Você VENCEU!')
  print('Vamos jogar novamente...')

print(macroSeparator)
print(f'GAME OVER! Você venceu {victory} vez(es).')
  