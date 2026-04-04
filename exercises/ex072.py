numbersinWords = (
  'zero',
  'um', 
  'dois', 
  'três', 
  'quatro', 
  'cinco', 
  'seis', 
  'sete', 
  'oito', 
  'nove', 
  'dez', 
  'onze', 
  'doze', 
  'treze', 
  'quatorze', 
  'quinze', 
  'dezesseis', 
  'dezessete', 
  'dezoito', 
  'dezenove', 
  'vinte'
)

while True:
  userNumber = int(input('Digite um número inteiro entre 0 e 20: '))
  
  if userNumber >= 0 and userNumber <= 20:
    break
  
  print('Número inválido, tente novamente!\n')
  
print('-' * 50)
print(f'Você digitou o número {numbersinWords[userNumber]}!')