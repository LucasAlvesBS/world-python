grade1 = float(input('Primeira nota: '))
grade2 = float(input('Segunda nota: '))

media = (grade1 + grade2) / 2
print(f'\nSua média foi de {media:.1f}!')

if media < 5:
    print('REPROVADO!')
elif 5 < media < 6.9:
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!')