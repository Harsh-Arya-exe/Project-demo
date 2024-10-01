class Employee:
    Employees = []
    emp_id = 0
    def __init__(self, name, age, salary, designation):
        self.name = name
        self.age = age
        self.salary = salary
        self.designation = designation
        Employee.emp_id += 1
        self.emp_id = Employee.emp_id
    
    def __str__(self):
        return (f"Name: {self.name}\nAge: {self.age}\nSalary: {self.salary}\n\
Designation: {self.designation}\nEmp_id:{self.emp_id}")
    
class EmployeeManagementSystem(Employee):
    def __init__(self):
        pass                    
    
    def add_employees(self):
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        salary = int(input("Enter salary: "))
        designation = input("Enter designation: ")
        emp = Employee(name, age, salary, designation)
        Employee.Employees.append(emp)
    
    def view_employees(self):
        for emps in Employee.Employees:
            print(f"\n{emps}\n")
    
    def update_emp_info(self, id):
        for emps in Employee.Employees:
            if emps.emp_id == id:
                new_name = input("Enter new name: ")
                new_age = int(input("Enter new age: "))
                new_salary = int(input("Enter new Salary: "))
                new_designation = input("Enter new Designation: ")
                emps.name = new_name
                emps.age = new_age
                emps.salary = new_salary
                emps.designation = new_designation

    def delete_employee(self,id):
        for emps in Employee.Employees:
            if emps.emp_id == id:
                Employee.Employees.remove(emps)
                Employee.emp_id -= 1
        print("Employee entry deleted")
while True:
        print("Employee Management System")
        print("\n1. Add Employee")
        print("2. View All Employees")
        print("3. Update Employee Information")
        print("4. Delete Employee")
        print("5. Exit")
        choice = int(input("Enter your choice (1-5): "))
        print("\n")
        
        if choice == 1:
            ems = EmployeeManagementSystem()
            ems.add_employees()
            pass
        if choice == 2:
            ems = EmployeeManagementSystem()
            ems.view_employees()
        if choice == 3:
            id = int(input("Enter emp id: "))
            ems = EmployeeManagementSystem()
            ems.update_emp_info(id)
        if choice == 4:
            id = int(input("Enter emp id: "))
            ems = EmployeeManagementSystem()
            ems.delete_employee(id)
        if choice == 5:
            break
