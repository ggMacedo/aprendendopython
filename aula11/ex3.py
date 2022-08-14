arquivo = open("1.txt", "r");

nome = input("Digite um nome de aluno para sua busca: ");
nomes = arquivo.read();
for linha in nomes:
    if(nome.lower() in nomes.lower().strip()):
        print("O aluno está matriculado");
    else:
        print("Aluno não matriculado");

    break;

arquivo.close();         
