#desafio 43
p=float(input("qual o seu peso? "))
a=float(input("qual a sua altura? "))
imc=p/(a*a)
print("o seu imc é de {}".format(imc))
if 18.5>=imc:
    print("você possui um baixo peso")
elif 18.6<imc<=24.9:
    print("você possui um peso normal")
elif 25<imc<=29.9:
    print("voce possui sobrepeso")
elif 30<imc<=34.9:
    print("você possui obesidade grau 1")
elif 35<imc<=39.9:
    print("você possui obesidade grau 2")
else:
    print("voce possui obesidade extrema")
