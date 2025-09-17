dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))

custoPorDia = dias * 60
custoPorKm = km * 0.15

totalAPagar = custoPorDia + custoPorKm

print('O total a pagar é de R${:.2f}'.format(totalAPagar))


# 1 km - R$0.15
#


# 1 dia - R$60
# dias - X