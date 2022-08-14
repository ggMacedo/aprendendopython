listaNome= []
listaIdade= []
i= 0;

while(i==0):
        listaNome.append(input("Digite o nome:" ))
        listaIdade.append(input("Digite a idade:" ))

        op = int(input("Deseja continuar cadastrando? (1 - SIM / 0 - NÃO): "))
        if(op == 0):
            i += 1
        else:
            i=0
for indice in range(len(listaNome)):
    print("Nome: ", listaNome[indice], "Idade: ", listaIdade[indice])
