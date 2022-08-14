soma = 0;
soma2 =0;
for indice in range(1, 11):
        valores = int(input("Digite o valor {}: ".format(indice)));
        if (valores >= 10) and (valores <=20):
            soma +=1;
        else:
            soma2 += 1;
print("Valores dentro do intervalo de 10 e 20: ", soma);
print("Valores fora do intervalo de 10 e 20: ", soma2);
        
