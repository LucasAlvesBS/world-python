equalSeparator = '=' * 40
hyphenSeparator = '-' * 40

totalPrice = totalProductsAbove1000 = cheapestProductPrice = count = 0
cheapestProductName = ''

print(equalSeparator)
print(' ' * 10 + 'LOJA SUPER BARATÃO')
print(equalSeparator)

while True:
  productName = str(input('Nome do produto: ')).strip()
  
  price = -1
  
  while price < 0:
    price = float(input('Preço: R$'))
  
  totalPrice += price
  
  if price > 1000:
    totalProductsAbove1000 += 1
    
  if count == 0 or price < cheapestProductPrice:
    cheapestProductPrice = price
    cheapestProductName = productName 
    
  count += 1  
  choice = 'A' 
  print(end='\n')
  
  while choice not in 'SN':
    choice = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    
  if choice == 'N':
    break
  
  print(hyphenSeparator)

print('\n========== FIM DO PROGRAMA ==========')
print(f'\nO total da compra foi de R${totalPrice:.2f}')
print(f'A quantidade de produtos custando mais de R$1000.00 é de {totalProductsAbove1000}')
print(f'O produto mais barato foi {cheapestProductName} que custa R${cheapestProductPrice:.2f}')
  
  