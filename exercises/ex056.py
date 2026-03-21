separator = '-=' * 40

print(separator)

print(' ' * 25 + 'INFORMAÇÕES PESSOAIS')

list_of_people = []
invalid_name_list = []
invalid_age_list = []
invalid_gender_list = []

minimum_characters = 2
maximum_years = 150
number_of_people = 4

for num in range(0, number_of_people):
    print(separator)
    print(f'Pessoa {num + 1}\n')

    name = str(input('Digite o nome: '))
    age = int(input('Digite a idade: '))
    gender = str(input('Digite o sexo (M/F): ')).strip().upper()[0]

    is_valid = True

    if len(name) <= minimum_characters:
        invalid_name_list.append(name)
        is_valid = False

    if age < 0 or age > maximum_years:
        invalid_age_list.append(age)
        is_valid = False

    if gender != 'M' and gender != 'F':
        invalid_gender_list.append(gender)
        is_valid = False

    if is_valid:
        list_of_people.append({'name': name, 'age': age, 'gender': gender})

print(separator)
print(' ' * 30 + 'LISTAS COLETADAS')
print(separator)

print(f'Lista de pessoas com informações válidas: {list_of_people}')
print(f'Lista com nomes inválidos: {invalid_name_list}')
print(f'Lista com anos inválidos: {invalid_age_list}')
print(f'Lista com gêneros inválidos: {invalid_gender_list}')

print(separator)

if len(list_of_people) < number_of_people:
    print(' ' * 35 + 'ERROS')
    print(separator)
    
    has_name_invalid = False
    has_age_invalid = False

    if len(invalid_name_list):
        has_name_invalid = True
        print(f'Existe(m) nome(s) inválido(s) na lista: {invalid_name_list}')
        print(f'Só são permitidos nomes com mais de {minimum_characters} caracteres!')

    if len(invalid_age_list):
        has_age_invalid = True

        if has_name_invalid:
            print(end='\n')

        print(f'Existe(m) anos(s) inválido(s) na lista: {invalid_age_list}')
        print(f'Só são permitidos anos inteiros positicos até {maximum_years} anos!')

    if len(invalid_gender_list):
        if has_name_invalid or has_age_invalid:
           print(end='\n')

        print(f'Existe(m) gênero(s) inválido(s) na lista: {invalid_gender_list}')
        print(f'Só são permitidos os gêneros masculino (M) ou feminino (F)!')
else:
    sum_of_age = 0
    older = 0
    names_of_the_elders = []
    female_reference_age = 20
    number_of_women_below_the_reference = 0

    for person in list_of_people:
        sum_of_age += person['age']

        if person['age'] > older:
            older = person['age']
            names_of_the_elders.clear()
            names_of_the_elders.append(person['name'])
        elif person['age'] == older:
            names_of_the_elders.append(person['name'])

        if person['gender'] == 'F' and person['age'] < female_reference_age:
            number_of_women_below_the_reference += 1

    average_age = sum_of_age / len(list_of_people)
    names = ', '.join(names_of_the_elders)

    if len(names_of_the_elders) > 1:
        sentence_form = 'As pessoas mais velhas são:'
    else:
        sentence_form = 'A pessoa mais velha é'
        
    print(' ' * 33 + 'RESULTADOS')
    print(separator)

    print(f'A média de idade do grupo é de {average_age:.1f} anos!')
    print(f'{sentence_form} {names} com {older} anos!')
    print(f'A quantidade de mulheres abaixo de {female_reference_age} anos é de {number_of_women_below_the_reference}!')



