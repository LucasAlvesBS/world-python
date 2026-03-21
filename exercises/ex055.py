list_of_weights = []
invalid_list = []

minimum_weight = 2
maximum_weight = 300

for num in range(0, 5):
    weight = float(input(f'Digite o peso (kg) da pessoa {num + 1}: '))
    list_of_weights.append(weight)

    if weight < minimum_weight or weight > maximum_weight:
        invalid_list.append(weight)

if len(invalid_list) > 0:
    print(f'\nExiste(m) peso(s) inválido(s) na lista: {invalid_list}\n')
    print(f'Só são permitidos pesos a partir de {minimum_weight} kg até o limite de {maximum_weight} kg!')
else:
    greater_weight = max(list_of_weights)
    lower_weight = min(list_of_weights)

    print(f'\nMaior peso: {greater_weight} kg')
    print(f'Menor peso: {lower_weight} kg')
