import random as rn

N=int(input('Δώστε έναν ακέραιο αριθμό: '))

l=[rn.randint(1,100) for i in range(N)]

for i in range(N-1):
    for j in range(N-1-i):
        if l[j+1]<l[j]:
            l[j],l[j+1]=l[j+1],l[j]

print(l)