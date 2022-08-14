def funcaoString(frase, mini, maxi):
    if(len(frase) >= mini and len(frase) <= maxi):
        return True;
    else:
        return False;

print(funcaoString("ABC", 0, 3));
