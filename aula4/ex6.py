nota = float(input("Digite a nota: "));
if (nota>= 0 and nota<= 10):
    if(nota >= 8):
        print("A");
    elif(nota>=7):
        print("B");
    elif(nota>=5):
        print("C");
    elif(nota>=3):
        print("D");
    else:
        print("E");
else:
    print("Nota inválida");
