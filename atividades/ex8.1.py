s = 0;
vetorNome = ["João", "Maria", "José"];
vetorNumero = ["934567869", "958762001", "976456002"]

def adicionaContato(nome, numero):
    vetorNome.append(nome);
    vetorNumero.append(numero);

    return print("Contato adicionado com sucesso!");

def modificaContato(indice, nome, numero):
    atualiza = False;
    for x in range(len(vetorNome)):
        if(x == indice):
            vetorNome[x] = nome;
            vetorNumero[x] = numero;
            atualiza = True;
           
    if(atualiza == True):
        return print("Contato {} atualizado com sucesso".format(indice));
    else:
        return print("Não foi possível atualizar o Contato {}".format(indice));
            
def excluiContato(indice):
    remocao = False;
    for x in range(len(vetorNome)):
        if(x == indice):
            del vetorNome[x];
            del vetorNumero[x];
            remocao = True;
            
    if(remocao == True):
        return print("Contato {} removido com sucesso".format(indice));
    else:
        return print("Não foi possível remover o Contato {}".format(indice));
             
while(s == 0):
    print("(1) adicionar contato\n (2) modificar contato\n (3) excluir contato\nCaso queira sair.Digite sair");
    op= input("Digite a opção desejada: ");
            
    if(op == "1"):
            
        adicionaContato(input("Digite o nome do contato: "), input("Digite o número do contato: "));
        for indice in range(len(vetorNome)):
            print(indice, "-", "Nome: ", vetorNome[indice], "Número: ", vetorNumero[indice]);
            
    elif(op == "2"):

        modificaContato(int(input("Informe o índice do contato que será modificado: ")), input("Digite o novo nome do contato: "), input("Digite o novo número do contato: "));
        for indice in range(len(vetorNome)):
            print(indice, "-", "Nome: ", vetorNome[indice], "Número: ", vetorNumero[indice]);
        
    elif(op == "3"):

        excluiContato(int(input("Informe o indíce do contato que será removido: ")));
        for indice in range(len(vetorNome)):
            print(indice, "-", "Nome: ", vetorNome[indice], "Número: ", vetorNumero[indice]);

    elif(op.lower() == "sair"):
        
        print("Obrigado por utilizar o sistema!");
        break;
    
    else:
        print("Opção inválida!");
