import re
import subprocess

def is_valid_ip(ip):
    pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
    return re.match(pattern, ip)

def is_pinging(ip):
    result = subprocess.run(["ping", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0

def write_to_file(file_name, content):
    with open(file_name, "a") as file:
        file.write(content + '\n')

def main():
    while True:
        user_input = input("Do you want to check an IP? (Yes/No): ").strip().lower()

        if user_input == "no" or user_input == "exit":
            with open("pinging_ips.txt", "r") as file:
                pinging_ips = file.read()
            with open("not_pinging_ips.txt", "r") as file:
                not_pinging_ips = file.read()
            print("Pinging IPs:")
            print(pinging_ips)
            print("Not Pinging IPs:")
            print(not_pinging_ips)
            break

        if user_input == "yes":
            ip = input("Enter an IP address: ")
            if is_valid_ip(ip):
                if is_pinging(ip):
                    write_to_file("pinging_ips.txt", ip)
                    print("IP is pinging and written to 'pinging_ips.txt'.")
                else:
                    write_to_file("not_pinging_ips.txt", ip)
                    print("IP is not pinging and written to 'not_pinging_ips.txt'.")
            else:
                print("Invalid IP address. Please enter a valid IP.")
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")


main()
