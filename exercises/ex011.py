width = float(input('Informe a largura: '))
height = float(input('Informe a altura: '))

area = width * height
ink = area / 2

print('Sua parede tem a dimensão de {}x{} e sua área é de {:.2f}m².'.format(width, height, area))
print('Para pintar essa parede, é necessária uma quantidade de {:.2f}l de tinta'.format(ink))

