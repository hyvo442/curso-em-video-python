import random
s0=str(random.randint(0,10))
print(f"{s0}")
s1=s0.split()
s2=str(input("digite um numero"))
s3=s2.split()
if s3==s1:
    print("parabens você acertou o numero")
else:
    print("você não acertou o numero")
