#desafio 40
nota1=float(input("qual a primeira nota?"))
nota2=float(input("qual a segunda nota?"))
if ((nota1+nota2)/2)<5:
  print("o aluno esta reprovado")
elif 5<=((nota1+nota2)/2)<7:
  print("o aluno esta de recuperacao")
else:
  print("o aluno esta aprovado")
