#desafio 89
lista_geral=[]
lista_notas=[]
alunos=0
while True:
    lista_geral2=[]
    lista_notas2=[]
    nome=input("nome")
    nota1=int(input('nota1:'))
    nota2=int(input("nota2:"))
    lista_geral2.append(nome)
    lista_geral2.append((nota1+nota2)/2)
    lista_notas2.append(nota1)
    lista_notas2.append(nota2)
    pergunta_break=input("quer continuar?")
    alunos+=1
    lista_geral.append(lista_geral2)
    lista_notas.append(lista_notas2)
    lista_geral2.clear
    lista_notas2.clear
    if pergunta_break=='n':
        break
lista_alunos=[]
print('Num nome media ',)
for c in lista_geral:
        print(alunos,end='   ')
        print(c[0],end='  ')
        print(c[1])
        lista_alunos.append(alunos)
        alunos-=1
while True:
    escolha=int(input("deseja ve as notas de algum aluno?"))
    if escolha not in lista_alunos:
         print("aluno nao encontrado")
    else:
        print(lista_notas[escolha-1])
    pergunta_break=input("quer continuar?")
    if pergunta_break=='n':
        break