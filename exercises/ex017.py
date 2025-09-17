from math import hypot, pow, sqrt

opposite = float(input('Digite o comprimento do cateto oposto: '))
adjacent = float(input('Digite o comprimento do cateto adjacente: '))

hypotenuse1 = hypot(opposite, adjacent)
hypotenuse2 = sqrt(pow(opposite, 2) + pow(adjacent, 2))

print('\nCom o cateto oposto de {} e o cateto adjacente de {}, '
      '\no comprimento da hipotenusa foi calculado de duas formas, \nsendo iguais a {:.2f} e {:.2f}!'
      .format(opposite, adjacent, hypotenuse1, hypotenuse2))
