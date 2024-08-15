n=int(input("Enter a number: "))

c=0
while(n>0):
    print(n%10)
    n=n//10
    c=c+1
print("digits: ",c)