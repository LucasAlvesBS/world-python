brazilianChampionshipTable = (
  'Palmeiras',
  'Fluminense',
  'Bahia',
  'São Paulo',
  'Athletico-PR',
  'Flamengo',
  'Coritiba',
  'Vasco',
  'Atlético-MG',
  'Grêmio',
  'Bragantino',
  'Vitória',
  'Santos',
  'Corinthians',
  'Botafogo',
  'Internacional',
  'Cruzeiro',
  'Chapecoense',
  'Mirassol',
  'Remo'
)

separator = '=' * 70
print(separator)
print(' ' * 7 + 'DADOS SOBRE O CAMPEONATO BRASILEIRO DE 2026 - 9ª RODADA')
print(separator)

print(f'Os 5 primeiros colocados são: {', '.join(brazilianChampionshipTable[:5])}')
print(f'\nOs 4 últimoos colocados da tabela são: {', '.join(brazilianChampionshipTable[16:])}')
print(f'\nTimes listados na ordem alfabética: {', '.join(sorted(brazilianChampionshipTable))}')
print(f'\nO time da Chapecoense está na {brazilianChampionshipTable.index('Chapecoense') + 1}ª posição')
