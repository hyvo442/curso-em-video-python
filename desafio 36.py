#desafio 36
casa=float(input("qual o valor da casa que você quer?"))
salario=float(input("quanto é o seu salário?"))
tempo=float(input("em quanto tempo em anos você planejar pagar a casa?"))
fatura=casa/(tempo*12)
if fatura<=salario*0.3:
     print(f" a casa foi liberada com uma parcela mensal de {fatura} reais")
else:
     print("a casa não foi liberada")
