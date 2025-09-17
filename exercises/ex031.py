distance = int(input('Digite a distância da viagem em km: '))

print(f'\nVocê está prestes a começar uma viagem de {distance:.1f}Km.')

if distance <= 200:
    price = distance * 0.50
else:
    price = distance * 0.45
# price = distance * 0.50 if distance <= 200 else distance * 0.45
print(f'O preço da passagem custará R${price:.2f}!')