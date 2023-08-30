import csv
from datetime import datetime, timedelta


file_path = "EMP_Details.csv"


today = datetime.now().strftime("%b %d")
print(today)


previous_dates = [(datetime.now() - timedelta(days=i)).strftime("%b %d") for i in range(1, 6)]


wfh_count_today = 0
wfo_count_today = 0
wfh_count_previous = 0
wfo_count_previous = 0
not_filled_employees = []

with open(file_path, "r") as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)

    today_index = None
    for col_index, date in enumerate(header[1:]):
        if date == today:
            today_index = col_index + 1
            break

    if today_index is not None:
        for row in csv_reader:
            for col_index, cell in enumerate(row[1:]):
                if cell == "WFH":
                    if col_index + 1 == today_index:
                        wfh_count_today += 1
                    elif header[col_index + 1] in previous_dates:
                        wfh_count_previous += 1
                elif cell == "WFO":
                    if col_index + 1 == today_index:
                        wfo_count_today += 1
                    elif header[col_index + 1] in previous_dates:
                        wfo_count_previous += 1
                elif all(not row[col_index + 1] for date in previous_dates):
                    not_filled_employees.append(row[0])
    else:
        print("Today's date not found in the CSV header.")

print("WFH & WFO Count on Current Date:")
print(f"WFH: {wfh_count_today}")
print(f"WFO: {wfo_count_today}")

print("\nWFH & WFO Count for Previous 5 Days:")
print(f"WFH: {wfh_count_previous}")
print(f"WFO: {wfo_count_previous}")

print("\nEmployees who haven't filled attendance for today and previous 5 days:")
print(not_filled_employees)
