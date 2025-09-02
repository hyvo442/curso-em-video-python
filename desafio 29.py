import random
s0=int(random.randint(70,200))
print(f"{s0}")
s1=(f"{(s0-80)*7}")
if s0>80:
      print("você vai pagar uma multa de {} reais pela multa".format (s1))
else:
    print("você nao paga multa")
