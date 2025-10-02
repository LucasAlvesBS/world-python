from datetime import  datetime

minimum_year = 1900
current_year = datetime.today().year

list_of_years = []
invalid_list = []

reference_age = 21
adulthood = 0
not_adulthood = 0

adulthood_list = []
not_adulthood_list = []

for num in range(0, 7):
    year = int(input(f'Digite o ano de nascimento da pessoa {num + 1}: '))
    age = current_year - year

    if year < minimum_year or year > current_year:
        invalid_list.append(year)
    else:
        list_of_years.append(year)

    if age >= reference_age:
        adulthood += 1
        adulthood_list.append(year)
    else:
        not_adulthood += 1
        not_adulthood_list.append(year)

if len(invalid_list) > 0:
    print(f'\nExiste(m) ano(s) de nascimento inválido(s) na lista: {invalid_list}\n')
    print(f'Só são permitidos anos a partir de {minimum_year} até o ano atual ({current_year})!')
else:
    print(f'\nMaioridade de referência: {reference_age} anos')

    adulthood_list.sort()
    print(f'\nQuantidade de pessoas maiores de idade: {adulthood}')
    print(f'Lista dos anos das pessoas maiores de idade: {adulthood_list}')

    not_adulthood_list.sort()
    print(f'\nQuantidade de pessoas menores de idade: {not_adulthood}')
    print(f'Lista dos anos das pessoas menores de idade: {not_adulthood_list}')



