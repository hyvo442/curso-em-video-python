#desafio 42
s0=int(input("diga o tamanho de uma reta"))
s1=int(input("diga o tamanho de outra reta"))
s2=int(input("diga o tamanho de outra reta"))
if s0+s1>s2 and s0+s2>s1 and s1+s2>s0:
  print("da pra fazer um triangulo",end="")
  if (s0+s1+s2)/3== s0 and (s0+s1+s2)/3== s1 and (s0+s1+s2)/3== s2:
    print(" e ele será um triângulo equilatero")
  elif s0==s1 and s1!=s2 and s0!=s2:
    print(" e ele sera um triangulo isosceles")
  elif s1==s2 and s1!=s0 and s2!=s0:
    print(" e ele sera  um triangulo isosceles")
  elif s2==s0 and s0!=s1 and s2!=s1:
    print("  ele sera um triangulo isosceles")
  else:
    print(" e ele será um triangulo escaleno")
else:
  print("nao da pra fazer um triangulo")
