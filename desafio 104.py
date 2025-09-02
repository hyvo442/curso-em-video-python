#Desafio 104
def leiaint():
    while True:
        try:
            numero=int(input("digite um numero"))
            print(f'numero validado ')
            break
        except ValueError:
            print('nao validado')
       
       
