print('Os números pares de 1 até 50 são:\n')

list = []

for number in range(2, 51, 2):
    list.append(str(number))
        
result = ' '.join(list)
print(result)