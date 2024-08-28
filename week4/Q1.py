def cal_sum_sub(a,b):
    add = a+b;
    diff = a-b;
    return "Sum : "+ str(add) + "Difference : " + str(diff);
    
a = int(input("Enter n1 : "))
b = int(input("Enter n2 : "))
print(cal_sum_sub(a,b))
