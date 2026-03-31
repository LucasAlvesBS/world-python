n = s = 0

while True:
  n = int(input('Digite um número: '))
  
  if n == 999:
    break
  
  s += n
  
print(f'A soma vale {s}')


name = 'José'
age = 33
salary = 987.3

print(f'O {name:-^20} tem {age} anos e ganha R$ {salary:.2f}!')

# name:->20   Alinhado à direita
# name:-<20   Alinhado à esquerda
