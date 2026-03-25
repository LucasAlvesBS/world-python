gender = ''

while gender != 'M' and gender != 'F':
  gender = str(input('Qual o sexo da pessoa? [M/F] ')).strip().upper()

print(f'O sexo da pessoa é: {gender}')