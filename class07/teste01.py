n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

summ = n1 + n2
sub = n1 - n2
mul = n1 * n2
div = n1 / n2
pot = n1 ** n2
wholeDiv = n1 // n2
rest = n1 % n2

print('A soma é {} e a subtração é {}\nA multiplicação é {} e a divisão é {:.3f}'.format(summ, sub, mul, div))
print('Enquanto que a potência é {}, a divisão inteira é {} e o resto é {}'.format(pot, wholeDiv, rest))