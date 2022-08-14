morango = float(input("Digite o valor de KG de morango: "));
maca = float(input("Digite o valor de KG de maçã: "));
totalMaca = 0;
totalMorango = 0;
totalFrutas = 0;

if(maca <= 5):
    totalMaca = maca * 2.50;
else:
    totalMaca = maca * 2.20;

if(morango <= 5):
    totalMorango = maca * 1.80;
else:
    totalMorango = maca * 1.50;

totalFrutas = (totalMaca + totalMorango);

if(maca + morango > 0 or totalFrutas > 25):
    totalFrutas = totalFrutas - (totalFrutas * 0.10);

print("O valor total a ser pago é de: ", round(totalFrutas,2));
