# desafio 71
retira = int(input("digite o valor que voce quer sacar"))
notas_50 = 0
notas_20 = 0
notas_10 = 0
notas_5 = 0
nota_1 = 0
while True:
    if retira >= 50:
        retira = retira-50
        notas_50 = notas_50+1
    if retira < 50 and retira >= 20:
        retira = retira-20
        notas_20 = notas_20+1
    if retira < 20 and retira >= 10:
        retira = retira-10
        notas_10 = notas_10+1
    if retira < 10 and retira >= 5:
        retira = retira-5
        notas_5 = notas_5+1
    if retira < 5 and retira > 0:
        retira = retira-1
        nota_1 = nota_1+1
    if retira == 0:
        break
print(
    f"no seu saque havera {notas_50} notas de 50 ,{notas_20} notas de 20 ,{notas_10} notas de 10 ,{notas_5} notas 5 e {nota_1} notas de 1 real")
