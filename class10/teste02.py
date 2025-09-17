nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota1 + nota2) / 2

print(f'Sua média foi {media:.2f}')

if media >= 6:
    print('Sua média foi boa.')
else:
    print('Sua média foi ruim.')

print('Parabéns!' if media >= 6 else 'Estude mais!')