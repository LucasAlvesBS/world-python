count = total = 0

while True:
  num = int(input('Digite um número (Para parar, digite 999): '))
  
  if num == 999:
    break
  
  total += num
  count += 1
  
print('-' * 50)
print(f'A quantidade de números digitados foi de {count} e a soma total deu {total}!')
  