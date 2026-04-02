separator = '-' * 40

totalOver18yearsOld = totalMen = totalWomenUnder20YearsOld = 0

while True:
  print(separator)
  print(' ' * 10 + 'CADASTRE UMA PESSOA')
  print(separator)
  
  age = int(input('Idade: '))
  gender = choice = 'A'
  
  while gender not in 'MF':
    gender = str(input('Sexo [M/F]: ')).strip().upper()[0]
    
  print(separator)
  
  if age > 18:
    totalOver18yearsOld += 1
  
  if gender == 'M':
    totalMen += 1
    
  if age < 20 and gender == 'F':
    totalWomenUnder20YearsOld += 1
  
  while choice not in 'SN':
    choice = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
     
  if choice == 'N':
    break

print('\n========== FIM DO PROGRAMA ==========')
print(f'\nTotal de pessoas com mais de 18 anos: {totalOver18yearsOld}')
print(f'Total de homens cadastrados: {totalMen}')
print(f'Total de mulheres com menos de 20 anos: {totalWomenUnder20YearsOld}')