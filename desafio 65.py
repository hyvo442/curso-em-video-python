#desafio 65pergunta='seila'
termos=1
numero=int(input("digite um numero"))
maior=0
menor=0
soma=numero
pergunta=''
while pergunta!='n':
    pergunta=input("deseja continuar")
    if termos==1:
            maior=numero
            menor=numero
    if pergunta=='s':
        numero=int(input("digite um numero"))
        termos=termos+1
        soma=soma+numero
    if termos>=2:
        if numero>maior:
            maior=numero
        if numero<menor:
            menor=numero
print(f"a media dos numeros que voce digitou é {soma/termos}")
print(f"o maior numero dos que voce digitou foi {maior} e o menor foi {menor}")
