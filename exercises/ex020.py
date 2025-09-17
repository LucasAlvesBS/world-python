from random import choice, shuffle

student1 = input('Digite o nome do primeiro aluno: ')
student2 = input('Digite o nome do segundo alune: ')
student3 = input('Digite o nome do terceiro aluno: ')
student4 = input('Digite o nome do quarto aluno: ')

students = [student1, student2, student3, student4]

line = '-' * 30

print(line)
print('Resolução do professor\n')

shuffle(students)
print(students)

print(line)
print('Minha resolução\n')

firstChosen = choice(students)
students.remove(firstChosen)

secondChosen = choice(students)
students.remove(secondChosen)

thirdChosen = choice(students)
students.remove(thirdChosen)

fourthChosen = choice(students)

print('A ordem de apresentação de trabalhos ficou da seguinte forma: ')
print(f'\n1º - {firstChosen}\n2º - {secondChosen}\n3º - {thirdChosen}\n4º - {fourthChosen}')




