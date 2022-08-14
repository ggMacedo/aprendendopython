saldo= 0;
i = 0;

while(i == 0):
    print("(1) consulta saldo\n (2) saque\n (3) depósito\n (4) sair");
    op= int(input("Digite a opção desejada: "));
            
    if(op == 1):
            
        print("Seu saldo é de: ", saldo);
            
    elif(op == 2):
        
        valorSaque= float(input("Digite o valor de saque: "));
        if(valorSaque > saldo):
            print("Você não tem saldo suficiente para este valor de saque!");
        else:
            saldo = saldo - valorSaque;
                        
    elif(op == 3):

        valorDeposito= float(input("Digite o valor de depósito: "));
        saldo = saldo + valorDeposito;

    elif(op == 4):
        
        print("Obrigado por utilizar o sistema!");
        break;
    
    else:
        print("Opção inválida!");
                    

