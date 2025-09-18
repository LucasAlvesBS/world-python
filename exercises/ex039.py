from datetime import datetime

gender = str(input('Digite o seu sexo (M/F): ')).upper().strip()[0]

if gender == 'M':
    yearOfBirth = int(input('Digite o ano de nascimento: '))
    currentYear = datetime.now().year

    age = currentYear - yearOfBirth
    print(f'\nSua idade é: {age} ano(s).')

    if age < 18:
        yearsToGo = 18 - age
        yearOfEnlistment = currentYear + yearsToGo
        print(f'Ainda vai se alistar no exército. Tempo que falta: {yearsToGo} ano(s).')
        print(f'Seu alistamento será no ano de {yearOfEnlistment}.')
    elif age == 18:
        print('É hora de se alistar no exército!')
    else:
        yearsHavePassed = age - 18
        yearOfEnlistment = currentYear - yearsHavePassed
        print(f'Já passou do tempo de alistamento. Tempo que passou: {yearsHavePassed} ano(s).')
        print(f'Seu alistamento foi no ano de {yearOfEnlistment}.')
elif gender == 'F':
    print('Você não precisa fazer o alistamento militar!')
else:
    print('Este é um gênero inválido. Tente novamente!')



