segment1 = float(input('Primeiro segmento: '))
segment2 = float(input('Segundo segmento: '))
segment3 = float(input('Terceiro segmento: '))

if segment1 + segment2 > segment3 and segment2 + segment3 > segment1 and segment3 + segment1 > segment2:
    if segment1 == segment2 and segment2 == segment3: # segment1 == segment2 == segment3
        print('Os segmentos formam um triângulo EQUILÁTERO!')
    elif segment1 == segment2 or segment2 == segment3 or segment3 == segment1:
        print('Os segmentos formam um triângulo ISÓSCELES!')
    else: # segment1 != segment2 != segment3 != segment1 (ESCALENO)
        print('Os segmentos formam um triângulo ESCALENO!')
else:
    print('Os segmentos NÃO PODEM formar um triângulo!')