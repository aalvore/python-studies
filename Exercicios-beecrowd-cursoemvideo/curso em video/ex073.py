tabela = ('flamengo', 'palmeiras', 'cruzeiro', 'fluminense', 'athleticopr', 'bahia', 'athleticomg', 'santos', 'bragantino',
          'SaoPaulo', 'Vasco', 'Botafogo', 'Coritiba', 'Mirassol', 'Corinthians', 'EcVitoria', 'Internacional', 'Gremio',
          'Remo', 'Chapecoense')

print(f'Os 5 primeiros colocados são {tabela[0:6]}')
print(f'Os ultimos 4 colocados sao {tabela[-4:]}')
print(f'Times em ordem alfabetica: {sorted(tabela)}')
print(f'O {tabela[-1]} Esta na {tabela.index('Chapecoense') + 1}a Posição')