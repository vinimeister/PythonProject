times = ('Palmeiras', 'Flamengo', 'Fluminense', 'Athletico-PR', 'Bragantino',
         'Bahia', 'Coritiba', 'SaoPaulo', 'Atletico-MG', 'Corinthians',
         'Cruzeiro', 'Botafogo', 'ECVitoria', 'Internacional', 'Santos',
         'Gremio', 'Vasco', 'Remo', 'Mirassol', 'Chapecoense')
print(f'Lista dos times do Brasileirão {times}')
print('=' * 100)
print(f'os 5 primeiros colocados são {times[0:5]}')
print('=' * 100)
print(f'os 4 times que estão na zona de rebaixamento são {times[16:20]}')
print('=' * 100)
print(sorted(times))
print(f'{times[19]} está em 20º posição ')
