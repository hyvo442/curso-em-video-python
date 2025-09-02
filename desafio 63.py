#desafio 63
termos=int(input("qual deve ser a posição do ultimo termo da  fibonacci?"))
primeiro=0
segundo=1
n=2
print(f"{primeiro}->{segundo}",end='')
while n!=termos:
    print('->',end='')
    terceiro=primeiro+segundo
    primeiro=segundo
    segundo=terceiro
    print(f"{terceiro}",end='')
    n=n+1
    
