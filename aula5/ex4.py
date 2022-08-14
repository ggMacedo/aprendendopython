n1 = float(input("Digite o valor 1: "));
n2 = float(input("Digite o valor 2: "));
n3 = float(input("Digite o valor 3: "));
if(n1 < (n2+n3) and n2 < (n1+n3) and n3 < (n1+n2)):
    
    if(n1 == n2 and n2 == n3):
        print("Triângulo equilátero");
    elif(n1 == n2 or n2 == n3):
        print("Triângulo isósceles");
    else:
        print("Triângulo escaleno");
        
else:
     print("Não forma um triângulo");
    
    
