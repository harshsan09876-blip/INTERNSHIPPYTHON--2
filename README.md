# INTERNSHIPPYTHON--2
after 12 days keep the internship continue.

# Day 12 – Palindrome Checker 🔄

## 📌 Task

Create a Python program that determines whether a word or sentence is a palindrome after normalizing the case and ignoring unnecessary spaces.

---

## 🎯 Objective

Practice:

- String manipulation
- String slicing
- String comparison
- Case normalization
- Handling spaces
- Conditional statements

---

## 🛠️ Tools Used

- Python
- VS Code

---

## 💡 Logic Used

1. Take a word or sentence as input from the user.
2. Convert the input into lowercase using `lower()`.
3. Remove unnecessary spaces using `replace()`.
4. Reverse the normalized string using string slicing `[::-1]`.
5. Compare the original normalized string with the reversed string.
6. Display whether the input is a palindrome or not.

---

## 💻 Python Code

```python
# Day 12 - Palindrome Checker

# Take input from the user
palindrome = input("Enter a word or sentence: ")

# Normalize the input
# Convert the input into lowercase
# Remove unnecessary spaces
normalized = palindrome.lower().replace(" ", "")

# Reverse the normalized string using slicing
reversed_text = normalized[::-1]

# Compare the normalized string with its reverse
is_palindrome = normalized == reversed_text

# Display the result
if is_palindrome:
    print("The input is a palindrome.")
else:
    print("The input is not a palindrome.")

c:\Users\user\OneDrive\Pictures\Screenshots\Screenshot 2026-09-04 114624.png


day - 13 
# Day 13 - Prime Number Analyzer

## 📌 Description

Build a Python program that checks whether a number is prime and generates all prime numbers within a specified range.

## 🎯 Objective

* Practice loops
* Practice conditions
* Practice functions
* Understand basic algorithmic thinking
* Learn optimized prime-number checking

## 🛠️ Tools Used

* Python
* VS Code

## 💡 My Logic

```text
# number input lena hai
# 0, 1 if not give the negative input
# for loop for iterations
# possible divisior honge toh phir prime no ka concept is over
# divisor mila toh False
# agar koi divisor nahi mila toh True
# number**0.5 se unnecessary divisibility checks avoid karna hai
# start number and ending number lena hai
# range ke andar har number ko check karna hai
# is_prime function ko reuse karna hai
```

## ⚙️ Algorithm

1. Take a number as input.
2. If the number is less than 2, return `False`.
3. Check possible divisors using a `for` loop.
4. Check divisibility using `%`.
5. If a divisor is found, return `False`.
6. Check only up to the square root of the number to avoid unnecessary checks.
7. If no divisor is found, return `True`.
8. Take a starting and ending number.
9. Check every number in the range using the reusable `is_prime()` function.
10. Display the prime numbers.

## 🧪 Example

```text
Enter a number: 17
Prime

Enter start number: 10
Enter ending number: 30

11 13 17 19 23 29
```

## 🧠 Interview Questions

### 1. What is a prime number?

A prime number is a number that is divisible only by 1 and itself.

### 2. How can the prime-checking algorithm be optimized?

First, check edge cases like 0 and 1. Then check divisibility only up to the square root of the number to avoid unnecessary checks.

### 3. What is algorithm complexity?

Algorithm complexity tells us how much time or memory an algorithm needs as the input size increases. It is commonly represented using Big O notation.

## 📊 Complexity

The optimized `is_prime()` function takes approximately:

**Time Complexity: O(√n)**

## 📚 Key Learning

* Functions
* `for` loops
* `if` conditions
* `%` modulo operator
* `return`
* Square-root optimization
* Function reuse
* Basic algorithm complexity

## ✅ Deliverables

* [x] Prime checker
* [x] Prime-number range generator
* [x] Algorithm explanation
* [x] Interview questions
* [x] Edge-case handling
day - 13 screenshot
![Day 13 Output](DAY_13_OUTPUT.png)


# 🌡️ Day 14 — Temperature Converter

## 📌 Description

A Python-based Temperature Converter that converts temperatures between **Celsius, Fahrenheit, and Kelvin**.

The program uses separate functions for each conversion and includes input validation and error handling.

---

## 🎯 Objective

The objective of this task is to practice:

* Python Functions
* Arithmetic Operations
* `return` statements
* `while` loops
* Conditional statements
* Input validation
* Exception handling using `try-except`
* Formatted output

---

## 🛠️ Tools Used

* Python
* VS Code / PyCharm
* Git & GitHub

---

## 🔄 Supported Conversions

The program supports six temperature conversions:

1. Celsius → Fahrenheit
2. Fahrenheit → Celsius
3. Fahrenheit → Kelvin
4. Kelvin → Fahrenheit
5. Celsius → Kelvin
6. Kelvin → Celsius

---

## 📐 Conversion Formulas

| Conversion           | Formula                   |
| -------------------- | ------------------------- |
| Celsius → Fahrenheit | `(C × 9/5) + 32`          |
| Fahrenheit → Celsius | `(F − 32) × 5/9`          |
| Fahrenheit → Kelvin  | `(F − 32) × 5/9 + 273.15` |
| Kelvin → Fahrenheit  | `(K − 273.15) × 9/5 + 32` |
| Celsius → Kelvin     | `C + 273.15`              |
| Kelvin → Celsius     | `K − 273.15`              |

---

## ⚙️ Program Logic

```text
Start
  ↓
Display conversion menu
  ↓
Take user's choice
  ↓
Validate choice
  ↓
Take temperature input
  ↓
Validate numeric input
  ↓
Check physically valid temperature
  ↓
Call appropriate conversion function
  ↓
Return converted value
  ↓
Display result
  ↓
Return to menu
  ↓
Exit when user selects 7
```

---

## 🧪 Input Validation

The program handles invalid inputs using `try-except`.

### Numeric validation

If the user enters something that cannot be converted into a number, the program displays an error message instead of crashing.

### Physical temperature validation

The program also checks absolute-zero limits:

* Celsius cannot be below `-273.15°C`
* Fahrenheit cannot be below `-459.67°F`
* Kelvin cannot be below `0 K`

---

## 💻 Sample Output

```text
===== Temperature Converter =====
1. Celsius → Fahrenheit
2. Fahrenheit → Celsius
3. Fahrenheit → Kelvin
4. Kelvin → Fahrenheit
5. Celsius → Kelvin
6. Kelvin → Celsius
7. Exit

Enter your choice: 1
Enter temperature: 25

25.00 °C = 77.00 °F
```

### Invalid Input Example

```text
Enter temperature: abc
Invalid input. Please enter a number.
```

### Invalid Kelvin Example

```text
Enter temperature: -10
Invalid temperature. Kelvin cannot be below 0.
```

---

## 🧠 Key Learning

Through this task, I learned how to:

* Break a program into reusable functions.
* Use parameters and return values.
* Apply temperature conversion formulas.
* Use `while` loops for repeated menu operations.
* Handle invalid user input with `try-except`.
* Validate physically meaningful temperature values.
* Format numerical output to two decimal places.

---

## 🎤 Interview Questions

### 1. Why use functions for repeated calculations?

Functions reduce code redundancy, make the program organized, and allow calculations to be reused whenever needed.

### 2. What is a `return` statement?

A `return` statement sends a value or result from a function back to the caller.

### 3. What happens when a function does not explicitly return a value?

Python automatically returns `None` when a function does not explicitly return a value.

---

## 📁 Project Structure

```text
Day-14/
│
├── temperature_converter.py
├── README.md
└── day-14-output.png
```

---

## 🚀 Conclusion

This project strengthened my understanding of **Python functions, mathematical operations, loops, input validation, and exception handling** while building a practical temperature conversion application.
## 📸 Sample Output

![Day 14 Output](day_14_output.png)


day - 15
# Day 15 – Python Contact Book

## 📌 Project Overview

This project is a simple Contact Book application built using Python.

The program allows users to add, view, search, and manage contact information using basic Python concepts.

## 🎯 Objective

- Practice Python functions
- Work with dictionaries
- Store and manage contact information
- Reduce code redundancy
- Implement user interaction

## 🛠️ Technologies Used

- Python
- VS Code

## ⚙️ Features

- Add a new contact
- View saved contacts
- Search for a contact
- Store contact details using a dictionary
- Simple menu-based interaction

## 🧠 Key Concepts Learned

- Functions
- Dictionaries
- Loops
- Conditional statements
- User input
- Dictionary operations

## 📂 Project Structure

```text
day-15--folder/
│
├── contact_book.py
├── day_15_output.png
└── README.md

# Day 16 – Scheduled Python Data Job

## 📌 Project Overview

This project demonstrates a simple scheduled Python data-processing job.

The program reads employee information from a CSV file, processes the data, displays the employee details, creates an output report, and logs the execution.

## 🎯 Objective

- Learn basic job scheduling and automation
- Process CSV data using Python
- Add execution logging
- Handle failed executions
- Make the job safe for repeated execution

## 🛠️ Technologies Used

- Python
- CSV
- Schedule
- Logging
- VS Code

## 📂 Project Structure

```text
day-16--folder/
│
├── data.csv
├── schedule_job.py
├── job.log
├── output_report.csv
├── day_16_output.png
└── README.md


# Day 17 - Email Report Automation System

## 📌 Project Overview

This project is part of the **Veda Technology Python Internship**.

The objective of this task is to generate a business report using Python and Pandas, save the report as an Excel file, and automate its delivery through email using SMTP.

The project also includes logging and error handling.

---

## 🎯 Objectives

* Generate a business report using Python.
* Use Pandas for data handling.
* Export the report to Excel.
* Learn the basics of SMTP email integration.
* Use environment variables for email credentials.
* Implement logging.
* Handle errors using `try-except`.

---

## 🛠️ Technologies Used

* Python
* Pandas
* OpenPyXL
* SMTP
* Excel
* Logging

---

## 📂 Project Structure

```text
Day_17_Email_Report_Automation/
│
├── email_report_automation.py
├── business_report.xlsx
├── email_automation.log
├── README.md
└── day-17-output.png
```

### File Description

| File                         | Purpose                          |
| ---------------------------- | -------------------------------- |
| `email_report_automation.py` | Main Python automation program   |
| `business_report.xlsx`       | Generated business report        |
| `email_automation.log`       | Stores program events and errors |
| `README.md`                  | Project documentation            |
| `day-17-output.png`          | Sample output screenshot         |

---

## 📊 Business Report

The program creates sample business data containing:

* Product
* Sales
* Revenue

The data is converted into a Pandas DataFrame and exported as:

```text
business_report.xlsx
```

The Excel report was successfully generated and opened for verification.

---

## 📧 Email Automation

The project uses Python's built-in `smtplib` library to connect to an SMTP server and send the generated Excel report as an attachment.

The program is designed to read email credentials through environment variables instead of storing credentials directly inside the Python code.

Example environment variables:

```text
EMAIL_ADDRESS
EMAIL_PASSWORD
RECIPIENT_EMAIL
```

No email credentials are hardcoded in the Python source code.

---

## 📝 Logging

Logging is used to record important events during program execution.

For example:

```text
Business report generated successfully.
Email sent successfully.
```

Errors are also recorded in:

```text
email_automation.log
```

---

## ⚠️ Current Testing Status

### Successfully Completed

* Python program executed successfully.
* Business data generated successfully.
* Pandas DataFrame created successfully.
* Excel report generated successfully.
* `business_report.xlsx` opened successfully.
* Logging and error handling added.
* `openpyxl` dependency resolved.
* `smtplib` availability confirmed.

### Pending

SMTP email delivery could not be completed because the SMTP server rejected the supplied authentication credentials.

The error occurred during SMTP authentication, not during Excel report generation.

Therefore, the report-generation portion of the automation is working, while the email-delivery portion requires further SMTP authentication setup.

---

## 🔐 Security

Email credentials should never be hardcoded in the Python source code.

Environment variables are used to keep credentials separate from the program.

Sensitive credentials should not be uploaded to GitHub or included in screenshots.

---

## 🎤 Interview Questions

### 1. How does SMTP work?

SMTP (Simple Mail Transfer Protocol) is a protocol used to send emails. A Python program can connect to an SMTP server, authenticate, and send an email to the recipient.

### 2. How should email credentials be stored?

Email credentials should not be hardcoded in the source code. They should be stored securely using environment variables or a secrets manager.

### 3. How would you handle email delivery failure?

I would use `try-except` to catch the error, record it using logging, and handle the failure without allowing the entire program to crash.

---

## 💡 Key Learning

This project helped me understand:

* Pandas DataFrame creation
* Excel report generation
* Python file handling
* SMTP concepts
* Environment variables
* Logging
* Exception handling
* Basic email automation

---

## ✅ Conclusion

The business report generation component of the project was successfully completed and verified through the generated Excel file.

SMTP integration was implemented in the Python program, but email delivery is currently pending due to SMTP authentication. This provided practical experience in debugging dependencies, authentication issues, and automation workflows.
 

![alt text](day-17--folder/business_excel.xlsx.png)

# Day 18 — Log Monitoring and Alert System

## 📌 Project Overview

This project is a **Log Monitoring and Alert System** built using Python.

The program is designed to monitor a continuously growing log file, detect `ERROR` patterns using Regular Expressions, count detected errors, and generate an alert when the configured error threshold is reached.

This project helped me practice **file processing, Regex, logging, and automation**.

---

## 🎯 Objective

* Monitor a continuously growing log file.
* Detect error patterns using Regex.
* Count detected errors.
* Configure an error threshold.
* Generate an alert when the threshold is reached.
* Record monitoring events using Python's `logging` module.

---

## 🛠️ Technologies Used

* Python
* Regular Expressions (`re`)
* `logging`
* File Handling
* `time`

---

## 📁 Project Structure

```text
Day_18/
│
├── application.log
├── log_monitor.py
├── monitor.log
└── README.md
```

### File Description

* **`application.log`** — Log file containing application information and error entries.
* **`log_monitor.py`** — Main Python script that monitors the log file.
* **`monitor.log`** — File used by Python's logging system to record monitoring events and alerts.
* **`README.md`** — Documentation for the project.

---

## ⚙️ How the Program Works

1. The program defines the log file, error threshold, and checking interval.
2. The `logging` module is configured to record events in `monitor.log`.
3. The program opens `application.log`.
4. `file.seek(0, 2)` moves the file pointer to the end of the existing log.
5. The program continuously waits for newly added log entries.
6. `readline()` reads newly available entries.
7. Regex checks the new line for the `ERROR` pattern.
8. When an error is detected, `error_count` increases.
9. When the error count reaches the configured threshold, an alert is generated.
10. The monitoring process continues until the program is stopped.

---

## 🔧 Configuration

The monitoring settings are configurable:

```python
LOG_FILE = "application.log"
ERROR_THRESHOLD = 3
CHECK_INTERVAL = 2
```

### `LOG_FILE`

Specifies the log file that the program monitors.

### `ERROR_THRESHOLD`

Defines the number of detected errors required to generate an alert.

### `CHECK_INTERVAL`

Defines the number of seconds the program waits before checking again when no new log entry is available.

---

## 🔎 Regex Pattern

The program uses:

```python
re.search(r"\bERROR\b", line, re.IGNORECASE)
```

This searches the newly added log line for the word `ERROR`.

The `re.IGNORECASE` option allows the program to recognize different letter cases such as `ERROR`, `Error`, and `error`.

---

## 📝 Logging

Python's `logging` module is configured using:

```python
logging.basicConfig(
    filename="monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
```

This allows monitoring information and alerts to be recorded in `monitor.log`.

---

## 🚨 Alert Mechanism

The program checks whether the number of detected errors has reached the configured threshold.

For example:

```text
ERROR 1
ERROR 2
ERROR 3
```

When the threshold is `3`, the system generates an alert:

```text
ALERT! Error threshold reached: 3 errors detected.
```

The alert is displayed in the terminal and recorded using the logging system.

---

## 🧪 Testing

The program is designed to monitor **newly added entries** rather than repeatedly processing the entire existing log file.

To test the monitoring system:

1. Run the program.
2. Keep the program running.
3. Add new `ERROR` entries to `application.log`.
4. Allow the monitor to detect the new entries.
5. Check the terminal for the alert.
6. Check `monitor.log` for recorded monitoring information.

---

## 🧠 What I Learned

Through this project, I learned:

* How to monitor a continuously growing file.
* How `seek()` can be used to position the file pointer.
* How to use Regex for pattern matching.
* How to count detected errors.
* How configurable thresholds work.
* How Python's `logging` module records events.
* How a continuous monitoring loop works.
* The basic concepts of log rotation and alert fatigue.

---

# 🎤 Interview Questions & Answers

### 1. How would you monitor a continuously growing log?

I would monitor a continuously growing log by opening the log file and tracking only newly added entries. I would use a configurable error threshold and check interval, and use Regex to detect error patterns. When the number of errors reaches the threshold, the system generates an alert.

### 2. What is log rotation?

Log rotation means managing log files when they become too large or too old. The current log can be archived or renamed and a new log file can be created so that storage does not grow indefinitely.

### 3. How can alert fatigue be reduced?

Alert fatigue can be reduced by avoiding repeated alerts, setting a proper error threshold, grouping similar errors, and adding a cooldown period between alerts.

---

## ▶️ How to Run

Open the terminal inside the `Day_18` folder and run:

```bash
python log_monitor.py
```

The program will start monitoring `application.log`.

Because the program continuously monitors the file, it can be stopped using:

```text
Ctrl + C
```

---

## 📸 Evidence

**Output evidence will be added after successful testing of the monitoring and alert mechanism.**

---

## ✅ Conclusion

This project provided practical experience with **Python file processing, Regular Expressions, logging, and automation**.

It also helped me understand how a basic monitoring system can detect error patterns in a continuously growing log and generate alerts based on a configurable threshold.

**Day 18 completed as part of my Python Programming Internship at Veda Technology.** 🚀


# Read and Process a Text File

## 📌 Project Overview

This project is a Python program that reads a text file and generates basic statistics from its content.

The program counts:

* Number of lines
* Number of words
* Number of characters

It also handles the situation where the requested file does not exist.

---

## 🎯 Objective

The main objective of this task is to practice:

* Python file handling
* `with open()` statement
* Reading a file line by line
* String processing using `split()`
* Counting using `len()`
* Exception handling with `FileNotFoundError`

---

## 🛠️ Technologies Used

* Python
* Text File (`.txt`)

---

## 📂 Project Structure

```text
Read-and-Process-a-Text-File/
│
├── text_statistics.py
├── practice.txt
└── README.md
```

---

## 📝 Input File

The `practice.txt` file contains sample text:

```text
Natsu Dragneel is the main character of the anime Fairy tail
miraculous ladybug is the wonderful show of 16-20 age group
```

---

## 💻 Program Logic

The program follows these steps:

1. Open the text file using `with open()`.
2. Initialize line, word, and character counters.
3. Read the file line by line using a `for` loop.
4. Increase the line counter for every line.
5. Use `split()` to separate words and count them.
6. Use `len()` to count characters.
7. Display the generated statistics.
8. Handle `FileNotFoundError` if the file does not exist.

---

## 🧩 Key Python Concepts

### `with open()`

The `with` statement automatically closes the file after the operation is completed.

### `split()`

`split()` separates a line into individual words.

### `len()`

`len()` is used to determine the number of items or characters.

### `FileNotFoundError`

This exception is handled when the requested text file cannot be found.

---

## 📊 Output

The program generates statistics based on the contents of `practice.txt`.

```text
Number of lines: 2
Number of words: ...
Number of characters: ...
```

> Note: The exact character count depends on whether newline characters are included in the calculation.

---

## ⚠️ Error Handling

If `practice.txt` does not exist, the program displays:

```text
File isn't found
```

This prevents the program from terminating unexpectedly because of a missing file.

---

# 🎤 Interview Questions & Answers

### 1. Why should files be opened using `with`?

The `with` statement automatically closes the file after the operation is completed. It makes file handling safer and prevents us from forgetting to close the file manually.

### 2. What is the difference between `read()`, `readline()`, and `readlines()`?

* `read()` reads the complete file content.
* `readline()` reads one line at a time.
* `readlines()` reads all lines and returns them as a list.

### 3. Why is exception handling important when working with files?

Exception handling prevents the program from crashing when problems occur, such as when a file does not exist or cannot be accessed.

---

## ✅ Learning Outcome

Through this task, I learned how to:

* Work with text files in Python
* Process files line by line
* Count lines, words, and characters
* Use `with open()` for safer file handling
* Handle missing files using exceptions
* Apply basic text-processing techniques

---

## 👨‍💻 Author

**Harsh Chauhan**

Python Programming Intern
Veda Technology

![alt text](image.png)


# Day 20 – CSV Data Processor

## 📌 Project Overview

This project is a **CSV Data Processor** developed as part of my Python Programming Internship at **Veda Technology**.

The program reads employee data from a CSV file and processes information such as employee names, departments, salaries, and performance.

It calculates useful statistics including total salary, average salary, highest salary, lowest salary, employee count, and average performance.

The program also handles missing or invalid values using Python exception handling.

---

## 🎯 Objective

The objective of this project is to learn practical CSV processing using Python.

The project focuses on:

* Reading CSV files
* Processing rows and columns
* Handling missing and invalid values
* Calculating statistics
* Generating a summary report
* Using Python's built-in `csv` module

---

## 🛠️ Tools Used

* Python
* `csv` module
* File Handling
* Exception Handling

---

## 📂 Project Structure

```text
day-20_folder/
│
├── employee.csv
├── csv_processor.py
└── summary_report.txt
```

### Files

**`employee.csv`**
Contains the employee dataset.

**`csv_processor.py`**
Reads and processes the CSV data and calculates the required statistics.

**`summary_report.txt`**
Contains the calculated summary generated by the Python program.

---

## 📄 Input Dataset

The CSV file contains the following columns:

```text
Name
Department
Salary
Performance
```

Example:

```csv
Name,Department,Salary,Performance
Harsh,CSE,160000,90
Jatin,CSE,120000,99
Sandeep,CSE,130000,80
Prabal,CSE,1230000,99
Munendra,CSE,49000,78
Azal,CSE,89000,89
Parth,CSE,180000,80
```

---

## ⚙️ How the Program Works

### 1. Read the CSV File

The program uses Python's built-in `csv` module to read `employee.csv`.

### 2. Process Employee Records

Each row is processed to obtain information such as salary and performance.

### 3. Validate Data

Salary and performance values are checked and converted into integers.

Missing or invalid values are handled using exception handling.

### 4. Calculate Statistics

The program calculates:

* Total number of employees
* Total salary
* Average salary
* Highest salary
* Lowest salary
* Number of valid salary records
* Number of invalid or missing salary records
* Average performance

### 5. Generate Summary Report

The calculated results are saved in:

```text
summary_report.txt
```

---

## 🧠 Error Handling

The program handles errors such as:

* CSV file not found
* Missing salary values
* Invalid salary values
* Invalid performance values

`try` and `except` are used to prevent invalid data from stopping the complete program.

---

## ▶️ How to Run

Open the terminal inside the `day-20_folder` directory and run:

```bash
python csv_processor.py
```

After successful execution, the program generates:

```text
summary_report.txt
```

---

## 📊 Output

The generated summary report contains the calculated employee and salary statistics.

Example output categories:

```text
Total Employees
Valid Salary Records
Invalid/Missing Salary Records
Total Salary
Average Salary
Highest Salary
Lowest Salary
Valid Performance Records
Average Performance
```

---

# 🎤 Veda Technology Interview Questions

## 1. What is CSV?

CSV stands for **Comma-Separated Values**.

It is a plain-text file format used to store tabular data. Data is organized into rows and columns, with values commonly separated by commas.

For example:

```text
Name,Department,Salary,Performance
Harsh,CSE,160000,90
```

---

## 2. How can Python read CSV files?

Python can read CSV files using its built-in **`csv` module**.

We can use `csv.reader()` or `csv.DictReader()` to read the data.

For example:

```python
import csv

with open("employee.csv", "r", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(row)
```

The `with open()` statement manages the file safely and automatically closes the file after the operation.

---

## 3. How would you handle missing values in a CSV?

Missing values can be handled by checking whether the field is empty before processing it.

Invalid values can also be handled using `try` and `except`.

For example:

```python
try:
    salary = int(salary_value)
except (ValueError, TypeError):
    # Handle invalid or missing value
    pass
```

This prevents invalid data from crashing the complete program.

---

## 🚀 Conclusion

This project helped me understand practical CSV processing using Python.

I learned how to read structured data, process employee records, validate values, handle errors, calculate statistics, and generate a summary report.

**Day 20 – CSV Data Processor Completed. 🐍🔥**
