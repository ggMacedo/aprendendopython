contadorM = 0;
contadorF = 0;
mediaGrupo = 0;
mediaGrupoM = 0;
mediaGrupoF = 0;
somaIdadeGrupo = 0;
somaIdadeGrupoM = 0;
somaIdadeGrupoF = 0;
i = 1;

while(i < 11):
        idade = int(input("Digite a idade da pessoa {}: ".format(i)));
        sexo = input("Digite o sexo da pessoa {} M ou F: ".format(i));
        
        if(sexo.upper() != "M") and (sexo.upper() != "F"):
             print("Sexo inválido!");
             continue;
            
        somaIdadeGrupo += idade;
        
        if (sexo.upper() == "M"):
            somaIdadeGrupoM += idade;
            contadorM += 1;
        elif (sexo.upper() == "F"):
             somaIdadeGrupoF += idade;
             contadorF += 1;
        i += 1;
             
mediaGrupo = somaIdadeGrupo / (contadorM + contadorF);
mediaGrupoM = somaIdadeGrupoM / contadorM;
mediaGrupoF = somaIdadeGrupoF / contadorF;
print("Idade media grupo: ", mediaGrupo);
print("Idade media grupo de homens: ", mediaGrupoM);
print("Idade media grupo de mulheres: ", mediaGrupoF);
        
