num = int(input("Enter an integer: "))
rev = 0
n = num
while (num != 0):
    rem = num % 10
    rev = rev * 10 + rem
    num = num/10
    
if (n == rev):
    print(rev, " is a palindrome.")
else:
    print(rev, " is not a palindrome.")

