#desafio 90
lista={'nome':'','nota1':'','nota2':'','situaçao':''}
n=input("qual o nome?")
lista['nome']=n
no1=int(input("qual a primeira nota?"))
lista['nota1']=no1
no2=int(input("qual a segunda nota?"))
lista['nota2']=no2
if ((no1+no2)/2)<7:
    lista['situaçao']='reprovado'
else:
    lista['situaçao']='aprovado'
print(lista)