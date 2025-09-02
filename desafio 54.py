#desafio 54
maior=0
menor=0
termo=int(input("quantas pessoas serao cadastradas?"))
for x in range(0,termo):
  idade=int(input(f"quando a {x+1}º pessoa nasceu?"))
  if 2025-idade>18:
    maior=maior+1
  else:
    menor=menor+1
print(f"{maior} sao maiores de idade e {menor} sao menores de idade")
