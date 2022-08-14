arquivo = open("alunos.txt", "r", encoding="utf-8");
for linha in arquivo:
    dados = linha.split(";");
    media = (float(dados[1]) + float(dados[2])) / 2;
    print("O aluno {} teve média de {}".format(dados[0], media));

arquivo.close();
