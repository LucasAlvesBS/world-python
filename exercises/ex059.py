separator = '-=-' * 15

print(separator)
print(' ' * 13 + 'MENU DE OPERAÇÕES')
print(separator)

print('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa')
print(separator)

option = 0

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
print(end='\n')

while option != 5:
  option = int(input('Escolha o número da operação no menu que deseja executar: '))
  
  if option == 1:
    total = num1 + num2
    print(f'\nA soma dos números equivale a {total}')
    
  elif option == 2:
    total = num1 * num2
    print(f'\nA multiplicação dos números equivale a {total}')
    
  elif option == 3:
    greater = max([num1, num2])
    print(f'\nO maior número é o {greater}')
    
  elif option == 4:
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    
  elif option == 5:
    print(f'\nVocê saiu do programa!')
    
  else: 
    print(f'\nEscolha uma operação válida que consta no menu!')
  
  print(separator)