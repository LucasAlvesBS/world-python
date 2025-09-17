from datetime import datetime

yearOfBirth = int(input('Digite o ano de nascimento: '))
currentYear = datetime.now().year

age = currentYear - yearOfBirth
print(f'\nSua idade é: {age} ano(s).')

if age < 18:
    yearsToGo = 18 - age
    print(f'Ainda vai se alistar no exército. Tempo que falta: {yearsToGo} ano(s)!')
elif age == 18:
    print('É hora de se alistar no exército!')
else:
    yearsHavePassed = age - 18
    print(f'Já passou do tempo de alistamento. Tempo que passou: {yearsHavePassed} ano(s)!')

