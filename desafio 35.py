s0=int(input("diga o tamanho de uma reta"))
s1=int(input("diga o tamanho de outra reta"))
s2=int(input("diga o tamanho de outra reta"))
if s0+s1>s2 and s0+s2>s1 and s1+s2>s0:
    print("da pra fazer um triangulo")
else:
    print("nao da pra fazer um triangulo")
