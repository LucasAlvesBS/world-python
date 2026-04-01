separator = '-' * 50

while True:
  num = int(input('Você quer ver a tabuadade de qual valor? '))
  print(separator)
  
  if num < 0:
    break
  
  for count in range(1, 11):
    result = num * count
    print(f'{num} x {count:2} = {result}')
    
  print('\nPara encerrar, digite um valor negativo!')
  print(separator)
  
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')