import math

#Θεωρούμε ότι ο χρήστης δίνει πραγματικούς αριθμούς από 0 έως 90
width1=(float(input('Δώστε το γεογραφικό πλάτος του πρώτου σημείου: ')))
length1=(float(input('Δώστε το γεογραφικό μήκος του πρώτου σημείου: ')))
width2=(float(input('Δώστε το γεογραφικό πλάτος του δευτέρου σημείου: ')))
length2=(float(input('Δώστε το γεογραφικό μήκος του δευτέρου σημείου: ')))

r=6372.8

dw=math.radians(abs(width1-width2))
dl=math.radians(abs(length1-length2))

a=math.sin((dw/2)**2)+math.cos(width1)*math.cos(width2)*math.sin((dl/2)**2)

c=2*math.asin((math.sqrt(a)))

d=r*c


print('Η απόσταση των δύο δωθέντων σημείων είναι: ',d)

