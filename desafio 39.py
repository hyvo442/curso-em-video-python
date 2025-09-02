#desafio 39
idade=int(input("qual ano voce nasceu"))
if (2025-idade)<18:
      print("você não precisa se alistar agora")
      print(f"ainda falta {18-(2025-idade)} ano(s)")
if (2025-idade)>18:
      print(f"você já devia ter feito o alistamento a {(2025-idade)-18} ano(s)")
else:
      print("voce já pode fazer o alistamento")
