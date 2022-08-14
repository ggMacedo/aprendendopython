base = float(input("Digite o valor da base do triângulo: "));
alt = float(input("Digite o valor da altura do triângulo: "));
if (base< 0 or alt< 0):
    print("Não pode conter valor menor que 0(negativo)");
else:
    result= (base * alt) / 2;
    print("O resultado da área é: ", result);
        
    
