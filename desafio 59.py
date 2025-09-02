q=int(input("digite um valor"))
q2=int(input("digite outro valor"))
j=int(input("digite '1' para somar, digite '2' para multiplicar, digite '3' para maior digite '4' para novos numeros, digite '5' para sair do programa"))
while j!=5:
  maior=q
  menor=q2
  if j==1:
    print(f'a soma dos numeros é igual a {q+q2}')
    j=int(input("digite '1' para somar, digite '2' para multiplicar, digite '3' para maior digite '4' para novos numeros, digite '5' para sair do programa"))
  if j==2:
    print(f'a multiplicacao dos termos é igual a {q*q2}')
    j=int(input("digite '1' para somar, digite '2' para multiplicar, digite '3' para maior digite '4' para novos numeros, digite '5' para sair do programa"))
  if j==3:
    if q<q2:
      print(f"o maior é {q2}")
      j=int(input("digite '1' para somar, digite '2' para multiplicar, digite '3' para maior digite '4' para novos numeros, digite '5' para sair do programa"))
    else:
      print(f"o maior é {q}")
      j=int(input("digite '1' para somar, digite '2' para multiplicar, digite '3' para maior digite '4' para novos numeros, digite '5' para sair do programa"))
  if j==4:
    q=int(input("digite um valor"))
    q2=int(input("digite outro valor"))
    j=int(input("digite '1' para somar, digite '2' para multiplicar, digite '3' para maior digite '4' para novos numeros, digite '5' para sair do programa"))
  if j>5:
    j=int(input("numero errado digitado,digite '1' para somar, digite '2' para multiplicar, digite '3' para maior digite '4' para novos numeros, digite '5' para sair do programa"))
