di={}
while True:
    x=input('Δώστε Αριθμό Μητρώου,Όνομα και για τερματισμό \'q\':')
    if x=='q':
        break
    num,name=x.split(',')
    am=int(num)
    di[am]=name

alist=[]
alist=sorted(di.items())
for tp in alist:
    print(tp[0],tp[1],sep='\t')