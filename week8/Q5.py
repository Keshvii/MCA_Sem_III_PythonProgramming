s = input("Enter string: ")

alph = []
dig = []

for c in s:
    if c.isdigit():
        dig.append(c)
    else:
        alph.append(c)

print(alph)
print(dig)
