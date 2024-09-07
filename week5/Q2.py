import random

s = input("Enter a String : ")
c = random.choices(s,k=1)

print(f"Random character from {s} : {c}")
