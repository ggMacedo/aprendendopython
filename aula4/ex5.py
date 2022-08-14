combus = input("Digite o tipo de combustível desejado: (G = Gasolina/A = Álcool)");

if (combus == "A" or combus == "a"):
    litros = float(input("Digite a quantidade de litros: "));
    if(litros <= 0):
        print("Valor de litros não pode ser zero ou menor que zero");
    else:
        if(litros<= 20):
            desc = (20/100) * 2.90;
            result = (2.90 * litros) - desc;
            print("Valor a ser pago com desconto: ", result);
        elif(litros>20):
            desc = (5/100) * 2.90;
            result = (2.90 * litros) - desc;
            print("Valor a ser pago com desconto: ", result);
    
elif (combus == "G" or combus == "g"):
     litros = float(input("Digite a quantidade de litros: "));
     if(litros <= 0):
        print("Valor de litros não pode ser zero ou menor que zero");
     else:
        if(litros<= 20):
            desc = (4/100) * 3.30;
            result = (3.30 * litros) - desc;
            print("Valor a ser pago com desconto: ", result);
        elif(litros>20):
            desc = (6/100) * 3.30;
            result = (3.30 * litros) - desc;
            print("Valor a ser pago com desconto: ", result);
else:
     print("Letra inválida no tipo de combustível");
     

