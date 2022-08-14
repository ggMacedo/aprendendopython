i = 0;

def adicao(n1, n2):
    return print("O resultado de {} + {} é {}".format(n1, n2, n1+n2));
    
def subtracao(n1, n2):
    return print("O resultado de {} - {} é {}".format(n1, n2, n1-n2));
  
def multiplicacao(n1, n2):
    return print("O resultado de {} * {} é {}".format(n1, n2, n1*n2));

def divisao(n1, n2):
    if(n1 != 0 or n2 != 0):
        return print("O resultado de {} / {} é {}".format(n1, n2, n1/n2));
    else:
        return print("Não é possível dividir por 0!");
            
while(i == 0):
    print("(+) adição\n (-) subtração\n (*) multiplicação\n(/) divisão\nCaso queira sair.Digite 0");
    op= input("Digite a opção desejada: ");
            
    if(op == "+"):
        try:   
            adicao(float(input("Digite o primeiro número da operação: ")), float(input("Digite o segundo número da operação: ")));
        except:
            print("Valor inválido!");
            
    elif(op == "-"):
        try:
            subtracao(float(input("Digite o primeiro número da operação: ")), float(input("Digite o segundo número da operação: ")));
        except:
            print("Valor inválido!");
        
    elif(op == "*"):
        try:
           multiplicacao(float(input("Digite o primeiro número da operação: ")), float(input("Digite o segundo número da operação: ")));
        except:
            print("Valor inválido!");


    elif(op == "/"):
        try:
            divisao(float(input("Digite o primeiro número da operação: ")), float(input("Digite o segundo número da operação: ")));
        except:
            print("Valor inválido!");

    elif(op == "0"):
        
        print("Obrigado por utilizar o sistema!");
        break;
    
    else:
        print("Opção inválida!");
