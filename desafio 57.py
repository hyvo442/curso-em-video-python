sexo=str(input("qual o seu sexo? [M/F]")).strip().upper()[0]
while sexo not in'MmFf':
  sexo=input("nao validade.Qual o seu sexo? [M/F]")
print("sexo cadastrado com sucesso")
