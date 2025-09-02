def pandas():
  import pandas
  dicionario={}
  numero_dados=0
  dados=0
  maior=0
  while True:
    coluna=input("qual o nome da coluna?")
    dicionario[f'{coluna}']=''
    while True:
      lista=[]
      while True:
        dados=dados+1
        dado=input("qual o dado?")
        lista.append(dado)
        dicionario[f'{coluna}']=lista
        break_dado=input("quer digitar mais dados para essa coluna?")
        while break_dado not in 'sn':
           break_dado=input("quer digitar mais dados para essa coluna?")
        if break_dado=='n':
          break
      if numero_dados==0:
        maior=dados
      else:
        if dados>maior:
          maior=dados
      dados=0
      numero_dados=numero_dados+1
      dicionario[f'{coluna}']=lista
      if break_dado=='n':
          break
    pergunta_break=input("quer continuar?")
    while pergunta_break not in 'sn':
           pergunta_break=input("quer digitar mais dados para essa coluna?")
    if pergunta_break=='n':
      break
  df = pandas.DataFrame(dicionario)
  for c in range(0,maior):
    print(df.loc[c])
pandas()