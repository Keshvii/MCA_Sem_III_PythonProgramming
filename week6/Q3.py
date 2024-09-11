n = int(input("Enter Number : "))
s = str(n)
size = len(s)
if(size==4):
    ans = int(s[0:2])**2 + int(s[2:])**2

    print(ans)
else:
    print("Enter 4-digit number!")