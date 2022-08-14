arquivo = open("ex4.txt", "w");
for i in range(1, 101):
    arquivo.write(str(i));
    arquivo.write("\n");

print("Arquivo criado com sucesso!");    
arquivo.close();
