wallet = float(input('Informe quanto a pessoa tem na carteira: '))

dollars = wallet / 5.43
euro = wallet / 6.35

print('Com R${:.2f}, a pessoa pode comprar US${:.2f} e €{:.2f}'.format(wallet, dollars, euro))