#Program to extract each digit from an integer in the reverse order.

n=int(input("Enter a number: "))

while(n>0):
    print(n%10)
    n=n//10
