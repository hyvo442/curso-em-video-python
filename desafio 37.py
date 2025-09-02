#desafio 37
numero=int(input("digite um numero"))
print('''digite:"
[1] para binario
[2] para octal 
[3] para hexadecimal''')
escolha=int(input("qual voce escolhe?"))
if escolha ==1:
    print(f"o numero {numero} em binario é {bin(numero)}")
elif escolha==2:
    print(f"o numero {numero} em octal é {oct(numero)}")
elif escolha==3:
    print(f"o numero {numero} em hexadecimal é {hex(numero)}")
else:
    print("essa opção não existe ")