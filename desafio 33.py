s0=int(input("digite um numero"))
s1=int(input("dgite outro numero"))
s2=int(input("digite outro numero"))
menor=s0
maior=s2
if s0>s1 and s1>s2:
    menor=s2
elif s0>s1 and s2>s1:
    menor=s1
if s0<s1 and s2<s1:
    maior=s1
elif s1<s0 and s2<s0:
    maior=s0
print("o maior numero é {} o menor numero é {}".format (maior,menor))
