s0=str(input("digite o seu nome"))
s1=s0.split()
s2=s1[0].count("santos")
print(f"{s2}")
if s2>0:
       print("o seu começa com santos")
else:
    print("o seu nome não começa com santos")
