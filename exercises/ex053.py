phrase = str(input('Digite uma frase: '))

transformed_phrase = phrase.upper().strip().replace(' ', '')
list_of_inverted_phrase = []

for letter in transformed_phrase:
    list_of_inverted_phrase.insert(0 ,letter)

inverted_phrase = ''.join(list_of_inverted_phrase)

print(transformed_phrase)
print(inverted_phrase)
print(f'\nA frase "{phrase}"', end=' ')

if transformed_phrase == inverted_phrase:
    print('é um POLÍNDROMO!')
else:
    print('NÃO é um políndromo!')
