#desafio 41
idade=int(input("quando o atleta nasceu?"))
if 2025-idade<=9:
  print("o atleta esta na categoria mirim")
elif 2025-idade<=14:
  print("o atleta esta na categoria infantil")
elif 2025-idade<=19:
  print("o atleta esta na categoria junior")
elif 2025-idade<=20:
  print("o atleta esta na categoria senior")
else:
  print("o atleta esta na categoria master")
