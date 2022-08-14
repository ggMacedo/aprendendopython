soma = 0;
for indice in range(1, 11):
        valores = int(input("Digite o valor {}: ".format(indice)));
        if (valores < 0):
            soma +=1;
print("Quantidade de valores negativos: ", soma);
