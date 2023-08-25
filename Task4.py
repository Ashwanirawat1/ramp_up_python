import random


def generate_employee_details(num_employees):
    cities = ["Kormangala", "HSR Layout", "Ballary", "Mumbai", "Chennai", "Nellore", "Gurgon", "Hyderabad"]
    for i in range(num_employees):
        emp_id = random.randint(1, 9999)
        emp_location = random.choice(cities)
        emp_salary = random.randint(20000, 150000)
        yield f"Emp Id: {emp_id}, Emp Location: {emp_location}, Emp Salary: {emp_salary}"


def main():
    try:
        num_employees = int(input("Enter the number of employee details to generate: "))
        if num_employees <= 0:
            print("Please enter a valid number greater than 0.")
            return

        employee_generator = generate_employee_details(num_employees)

        print("Employee Details:")
        for i in range(num_employees):
            employee_detail = next(employee_generator)
            print(employee_detail)
    except ValueError:
        print("Invalid input. Please enter a valid number.")


main()
