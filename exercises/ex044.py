price = float(input('Digite o valor do produto: R$'))

separator = '-=-' * 5

print(separator + ' Condição de Pagamento ' + separator)
print('(1) Dinheiro ou cheque \n(2) Cartão débito \n(3) Cartão crédito - 2x \n(4) Cartão crédito - 3x ou mais')
print(separator * 3)

payment_condition = int(input('Qual a condição de pagamento desejada? '))

if payment_condition < 0 or payment_condition > 5:
    print('Condição de pagamento inválida. Tente novamente!')
else:
    if payment_condition == 1:
        price_to_pay = price * (90 / 100)
        print('\n10% de desconto!')
    elif payment_condition == 2:
        price_to_pay = price * (95 / 100)
        print('\n5% de desconto!')
    elif payment_condition == 3:
        price_to_pay = price
        print('\nSem desconto!')
    else:
        price_to_pay = price * (120 / 100)
        print('\n20% de juros!')
    print(f'O total a ser pago será de R${price_to_pay:.2f}!')

