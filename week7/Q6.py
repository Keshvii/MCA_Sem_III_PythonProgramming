try:
    with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
        f1_lines = f1.readlines()
        f2_lines = f2.readlines()

    f1midline = f1_lines[len(f1_lines) // 2]
    f2lastline = f2_lines[-1]

    print(f1midline)
    print(f2lastline)

    f1_lines[len(f1_lines) // 2] = f2lastline
    f2_lines[-1] = f1midline


    with open("file1.txt", "w+") as f1, open("file2.txt", "w+") as f2:
        f1.writelines(f1_lines)
        f2.writelines(f2_lines)

    with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
        print("\nUpdated File1:")
        for line in f1:
            print(line, end="")
        print("\nUpdated File2:")
        for line in f2:
            print(line, end="")
        

except:
    print("file/s do not exist.")

