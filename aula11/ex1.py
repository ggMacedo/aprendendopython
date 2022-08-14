arquivo = open("1.txt", "w");
for i in range(1, 11):
    arquivo.write(input("Informe os nomes de cadastro {}: ".format(i) ));
    arquivo.write("\n");
    
arquivo.close();
