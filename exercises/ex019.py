from random import choice

student1 = input('Digite o nome do primeiro aluno: ')
student2 = input('Digite o nome do segundo aluno: ')
student3 = input('Digite o nome do terceiro aluno: ')
student4 = input('Digite o nome do quarto aluno: ')

chosen = choice([student1, student2, student3, student4])

print(f'\nO aluno escolhido foi {chosen}.')