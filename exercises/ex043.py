weight = float(input('Digite seu peso: '))
height = float(input('Digite sua altura: '))

imc = (weight / (height ** 2)) * 10000
print(f'\nIMC: {imc:.2f}')

if imc < 18.5:
    print('Abaixo do peso!')
elif 18.5 <= imc < 25:
    print('Peso ideal!')
elif 25 <= imc < 30:
    print('Sobrepeso!')
elif 30 <= imc < 40:
    print('Obesidade!')
else:
    print('Obesidade mórbida!')

