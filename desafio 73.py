#desafio 73
times=('fortaleza','juventde','cruzeiro','gremio','vasco','ceara','bragantino','corinthians','internacional','bahia','flamengo','botafogo','palmeiras','sao paulo','sport','atletico-mg','mirassol','santos','fluminense','vitoria')
print(f"os 5 primeiros colocados foram {times[0:5]}")
print(f"os ultimos 4 colocados foram {times[16:21]}")
print(f"os time em ordem alfabetica são {sorted(times)}")
print(f"o flamengo esta na {times.index('flamengo')+1}º posção")