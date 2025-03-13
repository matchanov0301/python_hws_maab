FILENAME = "employees.txt"


def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    position = input("Enter Position: ")
    salary = input("Enter Salary: ")

    with open(FILENAME, "a") as file:
        file.write(f"{emp_id},{name},{position},{salary}\n")

    print("Employee added successfully!\n")


def view_employees():
    try:
        with open(FILENAME, "r") as file:
            records = file.readlines()

        if not records:
            print("No employees found.\n")
            return

        print("\nEmployee Records:")
        for record in records:
            print(record.strip())
        print()

    except FileNotFoundError:
        print("No employee records found. Add some employees first!\n")


def search_employee():
    emp_id = input("Enter Employee ID to search: ")

    try:
        with open(FILENAME, "r") as file:
            for line in file:
                if line.startswith(emp_id + ","):
                    print("\nEmployee Found:", line.strip(), "\n")
                    return

        print("Employee not found.\n")

    except FileNotFoundError:
        print("No employee records found. Add some employees first!\n")


while True:
    print("Employee Records Manager")
    print("1. Add new employee")
    print("2. View all employees")
    print("3. Search for an employee")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        search_employee()
    elif choice == "4":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Try again!\n")
