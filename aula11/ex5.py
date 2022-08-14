arquivo = open("ex4.txt", "r");
arquivo1 = open("pares.txt", "w");
arquivo2 = open("impares.txt", "w");

for linha in arquivo:
    if(int(linha) % 2 == 0):
        arquivo1.write(linha);
    else:
        arquivo2.write(linha);

print("Arquivos criados com sucesso!");
arquivo.close();
arquivo1.close();
arquivo2.close();


