name = str(input('Digite seu nome: ')).strip()

if name == 'Lucas':
    print('Que nome bonito!')
elif name == 'Mateus' or name == 'Maria' or name == 'Pedro':
    print('Seu nome é bem popular no Brasil!')
elif name in 'Ana Clara':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal!')
print(f'Tenha uma bom dia, {name}!')