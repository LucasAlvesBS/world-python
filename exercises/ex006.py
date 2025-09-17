num = int(input('Digite um valor: '))

double = num * 2
triple = num * 3
squareRoot = num ** (1/2)

print('O dobro de {n} é {d}. \nO triplo de {n} é {t}. \nA raiz quadrada de {n} é {r:.2f}.'.format(n=num,d=double, t=triple, r=squareRoot))