words = (
  'aprender', 
  'programar', 
  'linguagem', 
  'python', 
  'curso', 
  'gratis', 
  'estudar',
  'praticar',
  'trabalhar',
  'mercado',
  'programador',
  'futuro',
)

vowels = ('a', 'e', 'i', 'o', 'u')

for index, word in enumerate(words):
  print(f'Na palavra {word.upper()} temos', end=' ')
  for letter in word:  
    for vowel in vowels:    
      if (vowel == letter):
        print(letter, end=' ')
  print(end='\n')
