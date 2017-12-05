def myrange(N,logos):
    x=1
    for i in range(N):
        yield x
        x=x*logos

for i in myrange(5,10):
    print(i)

for i in myrange(6,2):
    print(i)