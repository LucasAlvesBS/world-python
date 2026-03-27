num = total = 0
count = -1

while num != 999:
  total += num
  count += 1
  num = int(input('Digite um número (pra encerrar, digite 999): '))
  
print('-' * 70) 
print(f'A quantidade de números digitados foi de {count}')
print(f'A soma total entre esses números foi de {total}')
  