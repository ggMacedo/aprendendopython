nA = float(input("Digite o valor A: "));
nB = float(input("Digite o valor B: "));
nC = 0;
if (nA== 0 or nB== 0):
    print("Não pode conter valor 0");
else:
    if(nA > 0 and nB > 0):
        nC=30;
    elif(nA > 0 and nB< 0):
        nC =0;
    elif(nA > 0 and nB< 0):
        nC =-1;
    elif(nA > 0 and nB< 0):
        nC =nA*nB*(-1);
result = (nA**2) + (2*nA*nB) + (nB**2) + (nC**2* nA);
print(result);
        
