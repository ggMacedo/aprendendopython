arquivo = open("1.txt", "r");
i = 0;
for linha in arquivo:
    print("Nome:", linha.strip());
    i +=1;

print("O arquivo possue {} linhas.".format(i));
arquivo.close();  
