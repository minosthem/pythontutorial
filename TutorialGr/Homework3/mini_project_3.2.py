L=[]
while True:
    x=input('Δώστε έναν ακέραιο αριθμό ή Πληκτρολογήστε \'q\' για τερματισμό ή \'r\' για εξαγωγή δεδομένου από το τέλος της ουράς ή \'0r\' για εξαγωγή δεδομένου από την αρχή τη:')
    if x.isdigit():
        if x[0] == '0':
            x = x[1:]
            y = int(x)
            L[0:0] = [y]
            print(L)
        else:
            y = int(x)
            L.append(y)
            print(L)
    if x == 'q':
        break
    elif x == 'r' and not L == []:
        L.pop()
        print(L)
    elif x == '0r' and not L == []:
        L.pop(0)
        print(L)
    else:
        print('Λάθος. Παρακαλώ δοκιμάστε ξανά!')