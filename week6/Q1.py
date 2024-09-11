n1=int(input("Enter number of elements in tuple-1: "))
ls1 = []
for i in range(n1):
    ls1.append(int(input(f"element {i} : ")))

n2=int(input("Enter number of elements in tuple-2: "))
ls2 = []
for i in range(n2):
    ls1.append(int(input(f"element {i} : ")))    

tup1= tuple(ls1)
tup2 = tuple(ls2)
tup1 = tup1+tup2

print(tup1)
