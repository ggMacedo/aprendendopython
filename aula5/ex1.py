dataNasc = int(input("Digite seu ano de nascimento: "));
dataAtual = int(input("Digite o ano atual: "));
vota = dataAtual - dataNasc;
if (vota >= 16):
    print("Pode votar");
else:
    print("Não pode votar");
        
