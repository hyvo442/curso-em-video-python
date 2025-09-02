#desafio 99
def maior():
    while True:
        numero=int(input('numero:'))
        numeros_digitados=0
        maior=0
        if numeros_digitados==0:
            maior=numero
        else:
            if numero>maior:
                maior=numero
        numeros_digitados+=1
        perguta_break=input("deseja continuar?")
        while perguta_break not in 'sn':
            perguta_break=input("deseja continuar?")
        if perguta_break =='n':
            break
    print(f'{maior} é o maior numero digitado')
maior()
