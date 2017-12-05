di={}
while True:
    x=input('Δώστε Λέξη ή \'q\' για Έξοδο:')
    s=0
    if x=='q':
        break
    for i in x:
        if i=='Α' or i=='Ε' or i=='Η' or i=='Ι' or i=='Ν' or i=='Ο' or i=='Σ' or i=='Τ':
            s+=1
        elif i=='Κ' or i=='Π' or i=='Ρ' or i=='Υ':
            s+=2
        elif i=='Λ' or i=='Μ' or i=='Ω':
            s+=3
        elif i=='Γ' or i=='Δ':
            s+=4
        elif i=='Β' or i=='Φ' or i=='Χ':
            s+=8
        elif i=='Ζ' or i=='Θ' or i=='Ξ' or i=='Ψ':
            s+=10
    print('Πόντοι Λέξης:',s)
    di[x]=s

alist=[]
alist=sorted(di.items())
for tp in alist:
    print(tp[0],tp[1],sep='\t')