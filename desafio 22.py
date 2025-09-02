s0=input("digite o seu nome completo")
print("o seu nome em maiusculo é {}".format (s0.upper()))
print("o seu nome possui {} caracteres".format (len(s0.strip())))
print("o seu nome em minusculo é {}".format (s0.lower()))
s1=s0.split()
print(f"o seu primeiro nome possui {len(s1[0])} caracteres")

