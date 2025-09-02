import random
s0=int(random.randint(0,10))
print(f"{s0}")
s1=1
s2=int(input("digite um numero"))
if s0==s2:
  print("voce acertou parabens")
else:
  print("você não acertou o numero")
while s0!=s2:
  s2=int(input("tente dnv"))
  s1=s1+1
  if s0==s2:
    print("parabens você acertou o numero")
  else:
    print("você não acertou o numero")

print(f" voce preciou de {s1} vezes pra acertar")
