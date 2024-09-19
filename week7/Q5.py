file1 = open("Department.txt","r")
file2 = open("Employee.txt","r")
dept_emp = {}

for dept in file1:
    deptID = dept.split()
    dept_emp[deptID[0]]=[]

for emp_sal in file2:
    emp = emp_sal.split()  
    dept_emp[emp[3]].append(int(emp[2])) 

file1.close()
file2.close()

for dept_id, salaries in dept_emp.items():
    if len(salaries)>0:  
        avg_salary = sum(salaries) / len(salaries)
        print(f"Department ID: {dept_id}, Average Salary: {avg_salary:.2f}")
    else:
        print(f"Department ID: {dept_id}, No employees.")
