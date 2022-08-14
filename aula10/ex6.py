def funcaoStringLista(frase, vetor):
    achou = False;
    for i in vetor:
        if(i == frase):
            achou=  True;
            break;
        return achou;

vetor13 = ["A", "V", "YY", "ABC"];
print(funcaoStringLista("ABC", vetor13))
print(funcaoStringLista("oi", vetor13))
