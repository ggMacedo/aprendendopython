valor = -1;
while(valor != 0):
    
    try:
        valor = int(input("Digite o valor (maior que zero) ou zero para sair do programa: "));
    except:
        print("Valor inválido!");
    else:
        
        if(valor > 0):
            for i in (200, 100, 50, 20, 10, 1):
                if(valor >= i):
                    qtdNotas = valor / i;
                    print("A quantidade de notas de R${} é {}".format(i, int(qtdNotas)));
                    valor = valor %i;
            valor = -1;
