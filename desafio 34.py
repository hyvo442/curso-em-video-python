s0=float(input("qual o seu salário?"))
print(f"{s0}")
if s0>=1200:
    print("voce ira receber um bonus no seu salario de {}".format (s0*(10/100)))
else:
    print("voce ira receber um bonus no seu salario de {}".format (s0*(15/100)))
