#desafio 55
maior=0
menor=0
for v in range(1,6):
  peso=int(input(f"qual o peso da {v}º pessoa?"))
  if v==1:
    maior=peso
    menor=peso
  else:
      if peso>maior:
        maior=peso
      if peso<menor:
        menor=peso
print(f"o maior é {maior} e o menor é {menor}")
