class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"


class EmployeeManager:
    FILE_NAME = "employees.txt"

    def add_employee(self, employee):
        with open(self.FILE_NAME, "a") as file:
            file.write(str(employee) + "\n")
        print("Employee added successfully!")

    def view_all_employees(self):
        try:
            with open(self.FILE_NAME, "r") as file:
                records = file.readlines()
                if records:
                    print("Employee Records:")
                    for record in records:
                        print(record.strip())
                else:
                    print("No records found.")
        except FileNotFoundError:
            print("No records found.")

    def search_employee(self, employee_id):
        try:
            with open(self.FILE_NAME, "r") as file:
                for record in file:
                    if record.startswith(employee_id + ","):
                        print("Employee Found:")
                        print(record.strip())
                        return
            print("Employee not found.")
        except FileNotFoundError:
            print("No records found.")

    def update_employee(self, employee_id, name, position, salary):
        try:
            updated = False
            with open(self.FILE_NAME, "r") as file:
                records = file.readlines()

            with open(self.FILE_NAME, "w") as file:
                for record in records:
                    if record.startswith(employee_id + ","):
                        file.write(f"{employee_id}, {name}, {position}, {salary}\n")
                        updated = True
                    else:
                        file.write(record)

            print("Employee updated successfully!" if updated else "Employee not found.")
        except FileNotFoundError:
            print("No records found.")

    def delete_employee(self, employee_id):
        try:
            deleted = False
            with open(self.FILE_NAME, "r") as file:
                records = file.readlines()

            with open(self.FILE_NAME, "w") as file:
                for record in records:
                    if record.startswith(employee_id + ","):
                        deleted = True
                    else:
                        file.write(record)

            print("Employee deleted successfully!" if deleted else "Employee not found.")
        except FileNotFoundError:
            print("No records found.")


def main():
    manager = EmployeeManager()

    while True:
        print("\nEmployee Records Manager")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            position = input("Enter Position: ")
            salary = input("Enter Salary: ")
            manager.add_employee(Employee(emp_id, name, position, salary))

        elif choice == "2":
            manager.view_all_employees()

        elif choice == "3":
            emp_id = input("Enter Employee ID: ")
            manager.search_employee(emp_id)

        elif choice == "4":
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            position = input("Enter Position: ")
            salary = input("Enter Salary: ")
            manager.update_employee(emp_id, name, position, salary)

        elif choice == "5":
            emp_id = input("Enter Employee ID: ")
            manager.delete_employee(emp_id)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again!")


main()
