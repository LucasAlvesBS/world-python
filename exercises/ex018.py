from math import sin, cos, tan, radians

angle = float(input('Digite um ângulo: '))

sine = sin(radians(angle))
cosine = cos(radians(angle))
tangent = tan(radians(angle))

print('O ângulo {} tem o seno de {:.2f}, o cosseno de {:.2f} e a tangente de {:.2f}!'.format(angle, sine, cosine, tangent))