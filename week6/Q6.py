s = input("Enter a string : ")

up = []
lo = []
dig = []

for i in s:
    if i.isupper():
        up.append(i)
    elif i.islower():
        lo.append(i)
    else:
        dig.append(i)
        
print("Num. of Uppercase char: ", len(up))
print(up)
print("Num. of Lowercase char: ", len(lo))
print(lo)
print("Num. of alphabets: ", len(up)+len(lo))
print(up+lo)
print("Num. of digits: ", len(dig))
print(dig)
