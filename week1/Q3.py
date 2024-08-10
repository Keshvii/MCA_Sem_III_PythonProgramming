ans = []
for i in range(1,21):
    x = int(input("Enter an integer: "))
    if(x%5 == 0):
        ans.append(x)
print("Numbers divible by 5: ", ans)