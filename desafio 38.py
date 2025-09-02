#desaFio 38
numero1=int(input("digite um nunero"))
numero2=int(input("digite outro número"))
Maior=numero1
if numero1<numero2:
     Maior=numero2
     print(f"o Maior número é {numero2}")
elif numero1>numero2:
     print(f"o maior número é {numero1}")
else:
     print("os dois números são iguais")
