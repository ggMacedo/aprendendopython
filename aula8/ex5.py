valor = int(input("Digite o valor: "));

for i in (200, 100, 50, 20, 10, 1):
    if(valor >= i):
        qtdNotas = valor / i;
        print("A quantidade de notas de R${} é {}".format(i, int(qtdNotas)));
        valor = valor %i;

