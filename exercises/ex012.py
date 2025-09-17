value = float(input('Informe o preço do produto: R$'))

newValue = value * (95 / 100)
print('O produto de preço R${:.2f} com 5% de desconto tem o valor de R${:.2f}'.format(value, newValue))