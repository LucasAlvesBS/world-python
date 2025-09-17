from math import trunc

num = float(input('Digite um número real: '))

integer = trunc(num)

print('O número {} tem a parte inteira {}.'.format(num, integer))