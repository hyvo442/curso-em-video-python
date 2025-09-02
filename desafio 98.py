# desafio 98
def contador():
    for c in range(0, 11):
        print(f"{c}->", end='')
    print('fim')
    print('-'*30)
    for d in range(10, -1, -2):
        print(d, end=' ')
        print('->', end=' ')
    print('fim')
    inicio = int(input('qual o inicio?'))
    fim = int(input('qual o fim?'))
    contador = int(input("qual o metodo de contagem?"))
    for e in range(inicio, fim+1, contador):
        print(e, end='')
        print('->', end='')
    print('fim')


contador()
