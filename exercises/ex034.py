salary = float(input('Digite o salário: R$'))

if salary > 1250:
    newSalary = salary * (110 / 100)
else:
    newSalary = salary * (115 / 100)
print(f'Seu salário de R${salary:.2f} teve um aumento e agora será de R${newSalary:.2f}!')