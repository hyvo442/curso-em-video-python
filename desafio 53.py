#desafio 53
nome=str(input("digite uma palavra e saiba se ela é um palindromo: "))
y=nome.upper()
i=y.split()
h="".join(i)
print(f"{h[::-1]}")
if h==h[::-1]:
  print(f"{nome} é um palindromo")
else:
  print(f"{nome} não é um palindromo")
