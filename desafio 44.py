#desafio 44
preco=float(input("qual o preco do produto que voce quer?"))
forma_pagamento=int(input("se voce quer pagar com dinheiro em especie ou cheque digite 1 se quer pagalo no cartao digite 2"))
if preco>1:
  quebrado="reais"
else:
  quebrado="centavos"
if forma_pagamento==1:
  print("voce pagara apenas {} {}".format (preco*0.9,quebrado))
elif forma_pagamento==2:
  v0=int(input("se você quiser a pagar a vista no cartao digite 1 se quiser pagar em mais vezes digite o numero de parcelar que voce quer"))
  if v0==1:
    print("voce pagara apenas {} {}".format (preco*0.95,quebrado))
  elif v0==2:
    print(f"voce pagara {v0} parcelas de {preco/2} {quebrado}")
  else:
    print(f"voce pagara {v0} parcelas de {(preco*1.2)/v0} {quebrado}")
else:
  print("erro")
