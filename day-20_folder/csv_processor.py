import os
import csv

print("Current folder:", os.getcwd())
print("Files in current folder:", os.listdir())

input_file = "employee.csv"
output_file = "summary_report.txt"


def process_csv(filename):
    employees = 0
    valid_salary_count = 0
    invalid_salary_count = 0

    total_salary = 0
    salaries = []

    total_performance = 0
    valid_performance_count = 0

    try:
        with open(filename, "r", newline="") as f:
            reader = csv.DictReader(f)

            for row in reader:
                employees += 1

                # Read salary from CSV
                salary_value = row.get("Salary", "").strip()

                # Check whether salary is valid
                try:
                    salary = int(salary_value)

                    if salary >= 0:
                        total_salary += salary
                        salaries.append(salary)
                        valid_salary_count += 1
                    else:
                        invalid_salary_count += 1

                except (ValueError, TypeError):
                    invalid_salary_count += 1

                # Read performance from CSV
                performance_value = row.get("Performance", "").strip()

                try:
                    performance = int(performance_value)

                    if performance >= 0:
                        total_performance += performance
                        valid_performance_count += 1

                except (ValueError, TypeError):
                    pass

        # Calculate salary statistics
        if salaries:
            average_salary = total_salary / len(salaries)
            highest_salary = max(salaries)
            lowest_salary = min(salaries)
        else:
            average_salary = 0
            highest_salary = 0
            lowest_salary = 0

        # Calculate average performance
        if valid_performance_count > 0:
            average_performance = (
                total_performance / valid_performance_count
            )
        else:
            average_performance = 0

        # Create summary report
        report = f"""
CSV DATA PROCESSING SUMMARY
===========================

Total Employees: {employees}

SALARY STATISTICS
-----------------
Valid Salary Records: {valid_salary_count}
Invalid/Missing Salary Records: {invalid_salary_count}
Total Salary: {total_salary}
Average Salary: {average_salary:.2f}
Highest Salary: {highest_salary}
Lowest Salary: {lowest_salary}

PERFORMANCE STATISTICS
----------------------
Valid Performance Records: {valid_performance_count}
Average Performance: {average_performance:.2f}
"""

        with open(output_file, "w") as report_file:
            report_file.write(report)

        print("CSV file processed successfully!")
        print(f"Summary report created: {output_file}")
        print(report)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the CSV processor
process_csv(input_file)