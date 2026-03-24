from unidecode import unidecode
phrase = str(input('Digite uma frase: '))

transformed_phrase = phrase.upper().strip().replace(' ', '')
phraseWithoutAccent = unidecode(transformed_phrase)
list_of_inverted_phrase = []

for letter in phraseWithoutAccent:
    list_of_inverted_phrase.insert(0, letter)

inverted_phrase = ''.join(list_of_inverted_phrase)

# Solução alternativa mais simples
# inverted_phrase = phraseWithoutAccent[::-1]

print(phraseWithoutAccent)
print(inverted_phrase)
print(f'\nA frase "{phrase}"', end=' ')

if phraseWithoutAccent == inverted_phrase:
    print('é um PALÍNDROMO!')
else:
    print('NÃO é um palíndromo!')
