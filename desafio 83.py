#desafio 83
n=str(input("digite uma expressão usando parenteses"))
d=n.count("(")
e=n.count(")")
if d==e:
    print('a sentença é valida')
else:
    print('a senteça não é valida')