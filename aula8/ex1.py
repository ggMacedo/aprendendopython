maior = 0;
menor =0;
valores2 = 0;

for indice in range(1, 6):
        valores = int(input("Digite o valor {}: ".format(indice)));
        if(indice==1):
            maior = valores;
            menor = valores;
        
        if (maior < valores):
            maior =valores;
        elif(menor > valores):
            menor = valores;
            
print("O maior valor é: ", maior);
print("O menor valor é: ", menor);
