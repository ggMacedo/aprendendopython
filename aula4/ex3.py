n1 = int(input("Digite o primeiro número: "));
n2 = int(input("Digite o segundo número: "));
n3 = int(input("Digite o terceiro número: "));
if (n1 == 0 or n2 == 0 or n3 == 0):
    print("Não pode conter valor 0 nos números");
else:
    print("Primeiro número: ", n1);
    print("Segundo número: ", n2);
    print("Terceiro número: ", n3);

    #Maior
    if (n1 > n2 and n1 > n3):
        print("Primeiro é o número maior");
        
    elif(n2 > n1 and n2 > n3):
        print("Segundo é o número maior");

    elif(n3 > n1 and n3 > n2):
        print("Terceiro é o número maior");

    #Menor
    if (n1 < n2 and n1 < n3):
         print("Primeiro é o número menor");
        
    elif (n2 < n1 and n2 < n3):
         print("Segundo é o número menor");

    elif(n3 < n1 and n3 < n2):
        print("Terceiro é o número menor");
    

    
    
