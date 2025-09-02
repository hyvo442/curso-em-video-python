n=1
an=1
razao=int(input("qual a razão da pa"))
a1=int(input("qual o termo inicial da pa"))
while n!=10:
    an=a1+(n-1)*razao
    print(f'{an}',end='')
    print("->",end='')
    n=n+1
print("fim")