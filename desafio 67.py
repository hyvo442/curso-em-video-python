multiplicação=1
print(f"-------------------------------------------------------------------------------------------------------")
termo=int(input("quer ver a tabuada de qual valor?"))
print(f"-------------------------------------------------------------------------------------------------------")
while True:
    if termo<0:
        break
    tabuada=termo*multiplicação
    multiplicação=multiplicação+1
    print(f"{tabuada}")
    if multiplicação==11:
        print(f"-------------------------------------------------------------------------------------------------------")
        termo=int(input("quer ver a tabuada de qual valor?"))
        print(f"-------------------------------------------------------------------------------------------------------")
        multiplicação=1
print(f"programa encerrado")
    

