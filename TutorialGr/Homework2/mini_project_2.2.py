import random as rn

while True:
    x=rn.randint(0,36)
    if x==0:
        print('Κληρώθηκε το 0.')
    if x in range(1,18):
        if x in range(1,10,2):
            print('Μικρός,Κόκκινος,Μονός')
        elif x in range(2,11,2):
            print('Μικρός,Μαύρος,Ζυγός')
        elif x in range(11,18,2):
            print('Μικρός,Μαύρος,Μονός')
        else:
            print('Μικρός,Κόκκινος,Ζυγός')
    else:
        if x in range(19,28,2):
            print('Μεγάλος,Κόκκινος,Μονός')
        elif x in range(18,29,2):
            print('Μεγάλος,Μαύρος,Ζυγός')
        elif x in range(29,36,2):
            print('Μεγάλος,Μαύρος,Μονός')
        else:
            print('Μεγάλος,Κόκκινος,Ζυγός')

    y=input('Enter:Επόμενη Κλήρωση, \'q\'+Enter:Τερματισμός:')
    if y == '':
        continue
    elif y=='q':
        break

