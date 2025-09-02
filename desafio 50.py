termos=int(input("quantos termos?"))
soma=0
for s in range(0,termos):
    numero=int(input("numero:"))
    if numero %2==0:
        soma=soma+numero
print(f"a soma apenas dos numeros pares é {soma}")