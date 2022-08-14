media = 0;
soma =0;
contador = 0;
print("Média de 15 até 100:");
for indice in range(15, 101):
    soma += indice;
    contador += 1;
    
media = soma / contador;
print(media);
