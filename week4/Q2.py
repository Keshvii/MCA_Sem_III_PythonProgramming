def func(ls):
    n=len(ls)
    if(ls[0]==ls[n-1]):
        return True
    else:
        return False

ls = [1,2,3,4,5,6,1]
print("First and last elements of are same? ",func(ls))
