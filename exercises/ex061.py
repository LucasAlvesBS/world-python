separator = '-=' * 20

print(separator)
print(' ' * 9 + 'PROGRESSÃO ARITMÉTICA')
print(separator)

term = int(input('Digite o primeiro termo: '))
reason = int(input('Digite a razão: '))
termCounting = 1

while termCounting <= 10:
  print(term, end=' ')
  term += reason
  termCounting += 1
  