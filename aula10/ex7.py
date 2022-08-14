def mdc(a, b):
    if(b>0):
        return mdc(b, a%b);
    else:
        return a; 
print(mdc(12,20));
        
