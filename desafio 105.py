#desafio 105
def notas():
    dicionario={'quantidade de notas':'','maior nota':'','menor nota':'','media da turma':'','situação':''}
    quant_notas=0
    soma_notas=0
    maior=0
    menor=0
    media=0
    while True:
        nota=int(input('nota:'))
        if quant_notas==0:
            maior=nota
            menor=nota
        else:
            if nota>maior:
                maior=nota
            if nota<menor:
                menor=nota
        quant_notas=quant_notas+1
        soma_notas=soma_notas+nota
        pergunta_break=input("deseja continuar [s/n]")
        if pergunta_break=='n':
            break
    media=soma_notas/quant_notas
    dicionario['quantidade de notas']=quant_notas
    dicionario['maior nota']=maior
    dicionario['menor nota']=menor
    dicionario['media da turma']=media
    if media>=7:
        dicionario['situação']='Boa'
    if 5<media<7:
        dicionario['situação']='Razoavel'
    if media<5:
        dicionario['situação']='Ruim'
    print(dicionario)
notas()
    


        
        
