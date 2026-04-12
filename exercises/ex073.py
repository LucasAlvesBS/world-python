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

equalSeparator = '=' * 70
print(equalSeparator)
print(' ' * 7 + 'DADOS SOBRE O CAMPEONATO BRASILEIRO DE 2026 - 9ª RODADA')
print(equalSeparator)

hyphenSeparator = '-' * 70

print(f'Ranking de times: {', '.join(brazilianChampionshipTable)}')
print(hyphenSeparator)
print(f'Os 5 primeiros colocados são: {', '.join(brazilianChampionshipTable[:5])}')
print(hyphenSeparator)
print(f'Os 4 últimos colocados da tabela são: {', '.join(brazilianChampionshipTable[16:])}')
print(hyphenSeparator)
print(f'Times listados na ordem alfabética: {', '.join(sorted(brazilianChampionshipTable))}')
print(hyphenSeparator)
print(f'O time da Chapecoense está na {brazilianChampionshipTable.index('Chapecoense') + 1}ª posição')
