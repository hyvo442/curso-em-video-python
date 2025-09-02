termo=0
razao=int(input("qual a razao da pa"))
termo_inicial=int(input("qual o termo inicial"))
for posiçao in range(1,11):
      termo=termo_inicial+(posiçao-1)*razao
      print(f"{termo}",end=" " )
      print("->", end= " " )
print('fim')