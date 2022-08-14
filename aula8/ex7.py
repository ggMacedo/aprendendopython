divida = float(input("Informe o valor inicial da dívida: "));
jurosMensal = int(input("Informe o valor do juro mensal:"));
valorMensal = float(input("Informe o valor mensal de pagamento da dívida: "));
qtdMeses =0;
totalPago =0;
totalJuros = 0;

while(divida >0):
    
    porcDivida = divida * (jurosMensal / 100);
    divida += porcDivida;
    totalJuros += jurosMensal;
    
    if(divida > valorMensal):
        totalPago += valorMensal
        divida -= valorMensal;
    else:
        totalPago += divida;
        divida -= divida;
        
    qtdMeses += 1;
    
print("Quantidade de mêses: ", qtdMeses)
print("Valor total pago: ", round(totalPago, 2))
print("Valor total juros: ", round(totalJuros, 2))

    
