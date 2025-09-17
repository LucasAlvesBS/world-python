salary = float(input('Informe o salário do funcionário: R$'))

newSalary = salary * (115 / 100)
print('O salário do funcionário que ganhava R${:.2f}, com 15% de aumento, é de R${:.2f}'.format(salary, newSalary))