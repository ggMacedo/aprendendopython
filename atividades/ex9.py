nuSecreto = 123456;
nuUsuario = int(input("Digite o número secreto: "));
i = 3;

if(nuUsuario == nuSecreto):
    print("Você acertou o número secreto!!");
else:
    
    if(nuSecreto > nuUsuario):
        print("O número secreto é maior que o número digitado");
    elif(nuSecreto < nuUsuario):
         print("O número secreto é menor que o número digitado");
         
    while(i > 0):
        
        print("Você errou o número secreto!! Tem mais {} tentivas".format(i));
        nuUsuario = int(input("Digite o número secreto: "));

        if(nuUsuario == nuSecreto):
            print("Você acertou o número secreto!!");
            break;
        
        else:
        
            if(nuSecreto > nuUsuario):
                print("O número secreto é maior que o número digitado");
            elif(nuSecreto < nuUsuario):
                 print("O número secreto é menor que o número digitado");
                 
        i -= 1;
