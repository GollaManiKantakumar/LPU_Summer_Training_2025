class Employee:
    def __init__(self, emp_id, name, salary):
        self.__emp_id = emp_id
        self.__name = name
        self.__salary = salary

    def get_emp_id(self):
        return self.__emp_id

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def set_emp_id(self, emp_id):
        self.__emp_id = emp_id

    def set_name(self, name):
        self.__name = name

    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Salary cannot be negative.")

    def display_info(self):
        print("\n--- Employee Information ---")
        print("ID:", self.__emp_id)
        print("Name:", self.__name)
        print("Salary: ₹", self.__salary)

    def apply_salary_hike(self, percentage):
        if percentage > 0:
            hike = (percentage / 100) * self.__salary
            self.__salary += hike
            print(f"Salary increased by {percentage}%. New salary: ₹{self.__salary}")
        else:
            print("Invalid percentage. Hike should be positive.")

def main():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")

    while True:
        try:
            salary = float(input("Enter Salary: ₹"))
            if salary < 0:
                print("Salary must be non-negative.")
                continue
            break
        except ValueError:
            print("Please enter a valid numeric salary.")

    employee = Employee(emp_id, name, salary)

    while True:
        print("\n=== Menu ===")
        print("1. Display Employee Info")
        print("2. Give Salary Hike")
        print("3. Update Name")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            employee.display_info()

        elif choice == '2':
            try:
                percent = float(input("Enter hike percentage: "))
                employee.apply_salary_hike(percent)
            except ValueError:
                print("Please enter a valid numeric percentage.")

        elif choice == '3':
            new_name = input("Enter new name: ")
            employee.set_name(new_name)
            print("Name updated successfully.")

        elif choice == '4':
            print("Exiting Employee Management System.")
            break

        else:
            print("Invalid choice. Please enter 1 to 4.")

if __name__ == "__main__":
    main()
