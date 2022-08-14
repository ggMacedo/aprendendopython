nomes = [];

for i in range(1, 11):
    nomes.append(input("Digite o nome {}:".format(i)));

nomes.sort()
for i in range(10):
    for j in range(i+1, 10):
        if (nomes[i] >nomes[j]):
            aux = nomes[i]
            nomes[i] = nomes[j]
            nomes[j] = aux

print("Nomes em ordem alfabética")
for x in range(10):
    print(nomes[x])
