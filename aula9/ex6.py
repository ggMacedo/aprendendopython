vetorA = ["Flavio", "Gabriel", "Leo", "Carol"]
vetorB = [10, 5.5, 3.5, 9]
vetorC = [1, 2, 10, 6]
vetorD = []

for i in range(len(vetorB)):
    media = (vetorB[i] + vetorC[i]) / 2;
    vetorD.append(media);

for i in range(len(vetorD)):
    
    maior = max(vetorD);
    menor = min(vetorD);

    if (vetorD[i] == maior):
        print("Nome: ", vetorA[i], "P1: ", vetorB[i], "P2: ", vetorC[i], "Média: ", maior, "Situação Aprovado");
    elif (vetorD[i] == menor):
        print("Nome: ", vetorA[i], "P1: ", vetorB[i], "P2: ", vetorC[i], "Média: ", menor, "Situação Reprovado");


        

