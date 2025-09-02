s0=str(input("digite algo"))
s1=s0.count("a")
s2=s0.count("A")
s3=s1+s2
s4=s0.find("A")
s5=s0.find("a")
print("no que você escreveu aparece {} letra 'a' ou 'A'".format (s3))
if s4<s5:
    print("a letra 'A' começou no {}".format (s4))
elif s4>s5:
    print("a letra 'a' começou no {}".format (s5))
else:
    print("nao tem letra 'a' ou 'A' na frase")
s6=s0.rfind("A")
s7=s0.rfind("a")
if s6>s7:
    print("a ultima letra 'A' esta na posição {}".format (s6))
elif s6<s7:
    print("a ultima letra 'a' esta na posição {}".format (s7))
else:
    print("nao tem letra 'a' ou 'A'na frase")

