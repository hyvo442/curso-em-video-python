#desafio 72
numeros=('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quartoze','quinze','dezesseis','dezessete','dezoite','dezenove','vinte')
while True:
    escolhido=int(input("escolha um numero entra 0 e 20"))
    if 20>=escolhido>=0:
        break
print(f"o numero {escolhido} por extenso é {numeros[escolhido]}")