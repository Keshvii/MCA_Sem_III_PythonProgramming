file1 = open("Department.txt", "r")
file2 = open("Employee.txt", "r")
output = open("Emp_Dep.txt", "w")

departments = {}

for dept in file1:
    dept_data = dept.strip().split()
    departments[dept_data[0]] = (dept_data[1], dept_data[2])

for emp in file2:
    emp_data = emp.strip().split()
    eid, name, salary, did = emp_data[1], emp_data[0], emp_data[2], emp_data[3]

    if did in departments:
        dname, dlocation = departments[did]
        merged_line = f"{name} {eid} {salary} {did} {dname} {dlocation}\n"
        output.write(merged_line)

file1.close()
file2.close()
output.close()

print("Done!")

