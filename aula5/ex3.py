try:
    alt = float(input("Digite a altura: "));
    sexo = input("Digite o sexo(m/f): ");
except:
     print("Valor incorreto");
else:
    if(sexo.upper() == "M"):
        print("Peso ideal: ", (alt - 100) - (alt-150)/4);
    elif(sexo.upper() == "F"):
        print("Peso ideal: ", (alt - 100) - (alt-150)/2);
    else:
        print("Sexo inválido");
