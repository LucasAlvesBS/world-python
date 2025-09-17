phrase = input('Digite uma frase: ').strip()

letter = 'A'
upper = phrase.upper()

letterACount = upper.count(letter)
firstLetterA = upper.find(letter)
lastLetterA = upper.rfind(letter)

print(f'\nQuantidade de letra A na frase: {letterACount}')
print(f'Posição da primeira letra A na frase: {firstLetterA}')
print(f'Posição da última letra A na frase: {lastLetterA}')