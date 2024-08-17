import math
a = int(input("Enter lower range value : "))
b = int(input("Enter upper range value : "))

for j in range (a,b+1):
    isprime=True
    for i in range(2,int(math.sqrt(j))+1):
        if(j%i==0):
            isprime=False
            break;
        
    if(isprime):
        print(j);