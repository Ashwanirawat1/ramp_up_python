import re


def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)


def write_to_file(email):
    with open("email_list.txt", "w") as file:
        file.write(email + '\n')


def display_emails_from_file():
    try:
        with open("email_list.txt", "r") as file:
            email_list = file.read().splitlines()
            if email_list:
                print("Email IDs in the file:")
                for email in email_list:
                    print(email)
            else:
                print("No email IDs found in the file.")
    except FileNotFoundError:
        print("File 'email_list.txt' not found.")


def main():
    while True:
        try:
            user_input = input("Do you want to enter an email address? (Yes/No): ").strip().lower()

            if user_input == "no" or user_input == "exit":
                display_emails_from_file()
                break

            if user_input == "yes":
                email = input("Enter an email address: ")
                if is_valid_email(email):
                    write_to_file(email)
                    print("Email address is valid and written to file.")
                else:
                    print("Invalid email address. Please enter a valid email.")

            else:
                print("Invalid input. Please enter 'Yes' or 'No'.")

        except Exception as e:
            print("An error occurred:", e)


main()
