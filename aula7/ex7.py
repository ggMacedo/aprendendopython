continuar = "s";

while(continuar.lower() == "s"):
    numero = int(input("Digite o número:"));
    fatorial = numero;
    for i in range(numero-1, 0, -1):
        fatorial *= i;
    print("O fatorial de {} é {}".format(numero, fatorial));
    continuar = input("Deseja continuar? (s/n): ");
