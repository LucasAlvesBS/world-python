from datetime import datetime

yearOfBirth = int(input('Digite o ano de nascimento: '))
currentYear = datetime.today().year

age = currentYear - yearOfBirth
print(f'\nSua idade é: {age} anos')

if age <= 9:
    print('Categoria MIRIM!')
elif age <= 14:
    print('Categoria INFANTIL!')
elif age <= 19:
    print('Categoria JUNIOR!')
elif age <= 25:
    print('Categoria SENIOR!')
else:
    print('Categoria MASTER!')
