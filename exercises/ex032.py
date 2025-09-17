from datetime import datetime
year = int(input('Digite um ano para saber se é bissexto (Coloque 0 para ano atual): '))

if year == 0:
    year = datetime.now().year

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f'O ano {year} é bissexto!')
else:
    print(f'O ano {year} não é bissexto!')
