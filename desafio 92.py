lista={'nome':'','ano de nascimento':'','carteira de trabalho':''}
while True:
  lista['nome']=input("nome:")
  nascimento=int(input("ano de nascimento:"))
  lista['ano de nascimento']=nascimento
  carteira=input("vc possui carteira assinada? [s/n]")
  while carteira not in 'sn':
     carteira=input("vc possui carteira assinada? [s/n]")
  if carteira=='n':
    lista['carteira de trabalho']='nao tem'
    lista['idade']=2025-nascimento
    break
  else:
    lista['carteira de trabalho']='possui'
    lista['ano de contratação']=int(input('ano de contratação:'))
    lista['salario']=int(input("salario:"))
    lista['idade']=2025-nascimento
    lista['aposento']=60-(2025-nascimento)
    break
for k,v in lista.items():
  print(f'{k} {v}')