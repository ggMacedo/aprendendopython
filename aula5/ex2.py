try:
    nA = float(input("Digite o valor 1: "));
    nB = float(input("Digite o valor 2: "));
except:
     print("Valor incorreto");
else:
    op = input("Digite a operação desejada (+, -, *, /):");
    if (op== "+"):
        print(nA+nB);
    elif(op=="-"):
         print(nA-nB);
    elif(op=="*"):
        print(nA*nB);
    elif(op=="/"):
        
        if(nB == 0):
           print("Não é possível fazer divisão por zero.");
        else:
            print(nA/nB);
            
    else:
       print("Operação inválida");
     

        
