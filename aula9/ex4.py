disciplinasCC = ["LPA", "IPE", "CLD", "LM", "GA", "CE", "CLD", "IPE", "LPA"]
disciplinasSI = ["IPE", "LPA", "CE", "LM", "TGS", "LPA", "IPE"]
di = []

for i in disciplinasCC:
    if i not in di:
        di.append(i)
        
for i in disciplinasSI:     
    if i not in di:
        di.append(i)

print(di)

                   
                   
                   
