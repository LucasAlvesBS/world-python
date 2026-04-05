from random import randint

num1 = str(randint(0, 9))
num2 = str(randint(0, 9))
num3 = str(randint(0, 9))
num4 = str(randint(0, 9))
num5 = str(randint(0, 9))

tupleOfNumbers = (num1, num2, num3, num4, num5)

print(f'Os valores sorteados foram: {' '.join(tupleOfNumbers)}')
print(f'O maior valor sorteado foi {max(tupleOfNumbers)}')
print(f'O menor valor sorteado foi {min(tupleOfNumbers)}')
