import random as rn
import math

N=int(input('Πλήθος ακεραίων στη λίστα:'))
L=[rn.randint(1,21) for i in range(N)]

def stats(L):
    ''' (list)-->float,float '''
    mn=sum(L)/len(L)

    s=0
    for i in range(N):
        s=s+math.pow((L[i]-mn),2)
    sd=math.sqrt(s/(N-1))

    return mn,sd

mn,sd=stats(L)
print('Λίστα:',L)
print('Μέσος = {:5.2f},Τυπική απόκλιση = {:5.2f}'.format(mn,sd))