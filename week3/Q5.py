
def remove_chars(s,idx):
    s1=""
    for i in range(0,idx-1):
        s1=s1+s[i];
    return s1

s = input("Enter a string: ")
idx = int(input("Enter index: "))

print(remove_chars(s,idx))
