lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]
#maior = 0
#menor = 0
pares = []
primeiro = 0
#contador_primeiro = 0
#soma = 0
soma_negativos = 0
for i in lista:
    if primeiro == 0:
        primeiro = i
    #if i>maior:
    #    maior = i
    #if i<menor:
    #    menor = i
    if i%2==0:
        pares.append(i)
    #if i == primeiro:
    #    contador_primeiro += 1
    #soma += i
    if i < 0:
        soma_negativos += i    
print("a) ", max(lista))#print("a) ", maior)
print("b) ", min(lista))#print("b) ", menor)
print("c) ", pares)
print("d) ", lista.count(primeiro))#print("d) ", contador_primeiro)
print("e) ", round(sum(lista)/len(lista), 2))#print("e) ", round(soma/len(lista), 2))
print("f) ", soma_negativos)
