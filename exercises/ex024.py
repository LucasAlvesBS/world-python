city = str(input('Digite o nome da cidade: ')).strip()

upper = city.upper()
starts = upper.startswith('SANTO')

print(f'A cidade começa com SANTO? {starts}')