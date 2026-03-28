gender = ''

while gender != 'M' and gender != 'F':
  gender = str(input('Qual o sexo da pessoa? [M/F] ')).strip().upper()[0]
  
  if (gender != 'M' and gender != 'F'):
    print('Dado inválido! Digite um sexo válido!')

print(f'O sexo {gender} foi registrado com sucesso!')