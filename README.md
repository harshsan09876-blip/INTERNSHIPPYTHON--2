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


DAY - 21 - JSON PROCESSOR. 
# Day 21 — JSON Data Processor

## 📌 Project Overview

This project was completed as part of my **Python Programming Internship at Veda Technology**.

The objective of this task was to learn how to work with **JSON data in Python**, including reading structured data, searching records, and displaying candidate information.

---

## 🎯 Objective

* Understand JSON and its structure.
* Learn how to read JSON data using Python.
* Use the built-in `json` module.
* Search for a particular candidate.
* Work with lists and dictionaries.
* Handle JSON file processing using Python.

---

## 🛠️ Technologies Used

* **Python**
* **JSON**
* **`json` module**

---

## 📂 Project Structure

```text
DAY_21/
│
├── data.json
└── python.py
```

### `data.json`

The JSON file stores candidate information such as:

* Name
* Class
* Roll Number
* Subject
* CGPA Status

### `python.py`

The Python script reads the JSON file and allows the user to search for a candidate by name.

---

## ⚙️ How the Program Works

```text
data.json
    ↓
json.load()
    ↓
Python List of Dictionaries
    ↓
User enters candidate name
    ↓
Search candidate
    ↓
Display candidate information
```

The program uses `json.load()` to read the JSON file and convert the JSON data into Python objects.

The search is made **case-insensitive** by using `.lower()`.

---

## 💻 Main Concepts Used

### `json.load()`

Used to read JSON data from a file.

```python
with open("data.json", "r") as file:
    candidate = json.load(file)
```

### Searching

The program compares the entered name with the candidate's name:

```python
if i["name"].lower() == search.lower():
```

### Key-Value Structure

Each candidate is represented using key-value pairs:

```text
"name" → "Harsh"
"class" → "CSE"
"rollno" → 20
"subject" → "COA"
"cgpa_status" → "Pass"
```

---

## 🖥️ Sample Output

```text
Enter the candidate name: Harsh

Candidate Found!
Name: Harsh
Class: CSE
Roll No: 20
Subject: COA
CGPA Status: Pass
```

If the candidate does not exist:

```text
Enter the candidate name: Rahul

Candidate not found.
```

---

## 🧠 What I Learned

Through this task, I learned:

* What JSON is.
* Difference between JSON and a Python dictionary.
* How to read JSON files using `json.load()`.
* How JSON data becomes Python lists and dictionaries.
* How to search structured data.
* How to access dictionary values using keys.
* Why `with open()` is useful for file handling.
* How to perform case-insensitive searching.

---

## 🎤 Interview Questions & Answers

### 1. What is JSON?

**Answer:**

> JSON stands for JavaScript Object Notation. It is a lightweight data format used to store and exchange structured data. It is commonly used for communication between frontend and backend applications.

### 2. What is the difference between JSON and a Python dictionary?

**Answer:**

> A Python dictionary is a data structure used inside Python to store data in key-value pairs. JSON is a language-independent data format used to store and exchange structured data.

### 3. How do you read JSON from a file in Python?

**Answer:**

> We use `json.load()` to read JSON data from a file. We open the file using `with open()` and then use `json.load(file)` to convert the JSON data into Python objects such as a list or dictionary.

---

## 🔑 Important Difference

```text
json.load()  → Read JSON from a file
json.dump()  → Write JSON to a file
```

---

## 👨‍💻 Internship Information

**Internship:** Python Programming Internship
**Organization:** Veda Technology
**Task:** Day 21 — Create a JSON Data Processor
**Language:** Python

---

## ✅ Conclusion

The Day 21 project helped me understand how Python can process **structured JSON data**. I learned how to read JSON files, work with lists and dictionaries, search records, and display relevant information based on user input.
# Day 21 — JSON Data Processor

## 📌 Project Overview

This project was completed as part of my **Python Programming Internship at Veda Technology**.

The objective of this task was to learn how to work with **JSON data in Python**, including reading structured data, searching records, and displaying candidate information.

---

## 🎯 Objective

* Understand JSON and its structure.
* Learn how to read JSON data using Python.
* Use the built-in `json` module.
* Search for a particular candidate.
* Work with lists and dictionaries.
* Handle JSON file processing using Python.

---

## 🛠️ Technologies Used

* **Python**
* **JSON**
* **`json` module**

---

## 📂 Project Structure

```text
DAY_21/
│
├── data.json
└── python.py
```

### `data.json`

The JSON file stores candidate information such as:

* Name
* Class
* Roll Number
* Subject
* CGPA Status

### `python.py`

The Python script reads the JSON file and allows the user to search for a candidate by name.

---

## ⚙️ How the Program Works

```text
data.json
    ↓
json.load()
    ↓
Python List of Dictionaries
    ↓
User enters candidate name
    ↓
Search candidate
    ↓
Display candidate information
```

The program uses `json.load()` to read the JSON file and convert the JSON data into Python objects.

The search is made **case-insensitive** by using `.lower()`.

---

## 💻 Main Concepts Used

### `json.load()`

Used to read JSON data from a file.

```python
with open("data.json", "r") as file:
    candidate = json.load(file)
```

### Searching

The program compares the entered name with the candidate's name:

```python
if i["name"].lower() == search.lower():
```

### Key-Value Structure

Each candidate is represented using key-value pairs:

```text
"name" → "Harsh"
"class" → "CSE"
"rollno" → 20
"subject" → "COA"
"cgpa_status" → "Pass"
```

---

## 🖥️ Sample Output

```text
Enter the candidate name: Harsh

Candidate Found!
Name: Harsh
Class: CSE
Roll No: 20
Subject: COA
CGPA Status: Pass
```

If the candidate does not exist:

```text
Enter the candidate name: Rahul

Candidate not found.
```

---

## 🧠 What I Learned

Through this task, I learned:

* What JSON is.
* Difference between JSON and a Python dictionary.
* How to read JSON files using `json.load()`.
* How JSON data becomes Python lists and dictionaries.
* How to search structured data.
* How to access dictionary values using keys.
* Why `with open()` is useful for file handling.
* How to perform case-insensitive searching.

---

## 🎤 Interview Questions & Answers

### 1. What is JSON?

**Answer:**

> JSON stands for JavaScript Object Notation. It is a lightweight data format used to store and exchange structured data. It is commonly used for communication between frontend and backend applications.

### 2. What is the difference between JSON and a Python dictionary?

**Answer:**

> A Python dictionary is a data structure used inside Python to store data in key-value pairs. JSON is a language-independent data format used to store and exchange structured data.

### 3. How do you read JSON from a file in Python?

**Answer:**

> We use `json.load()` to read JSON data from a file. We open the file using `with open()` and then use `json.load(file)` to convert the JSON data into Python objects such as a list or dictionary.

---

## 🔑 Important Difference

```text
json.load()  → Read JSON from a file
json.dump()  → Write JSON to a file
```

---

## 👨‍💻 Internship Information

**Internship:** Python Programming Internship
**Organization:** Veda Technology
**Task:** Day 21 — Create a JSON Data Processor
**Language:** Python

---

## ✅ Conclusion

The Day 21 project helped me understand how Python can process **structured JSON data**. I learned how to read JSON files, work with lists and dictionaries, search records, and display relevant information based on user input.
# Day 21 — JSON Data Processor

## 📌 Project Overview

This project was completed as part of my **Python Programming Internship at Veda Technology**.

The objective of this task was to learn how to work with **JSON data in Python**, including reading structured data, searching records, and displaying candidate information.

---

## 🎯 Objective

* Understand JSON and its structure.
* Learn how to read JSON data using Python.
* Use the built-in `json` module.
* Search for a particular candidate.
* Work with lists and dictionaries.
* Handle JSON file processing using Python.

---

## 🛠️ Technologies Used

* **Python**
* **JSON**
* **`json` module**

---

## 📂 Project Structure

```text
DAY_21/
│
├── data.json
└── python.py
```

### `data.json`

The JSON file stores candidate information such as:

* Name
* Class
* Roll Number
* Subject
* CGPA Status

### `python.py`

The Python script reads the JSON file and allows the user to search for a candidate by name.

---

## ⚙️ How the Program Works

```text
data.json
    ↓
json.load()
    ↓
Python List of Dictionaries
    ↓
User enters candidate name
    ↓
Search candidate
    ↓
Display candidate information
```

The program uses `json.load()` to read the JSON file and convert the JSON data into Python objects.

The search is made **case-insensitive** by using `.lower()`.

---

## 💻 Main Concepts Used

### `json.load()`

Used to read JSON data from a file.

```python
with open("data.json", "r") as file:
    candidate = json.load(file)
```

### Searching

The program compares the entered name with the candidate's name:

```python
if i["name"].lower() == search.lower():
```

### Key-Value Structure

Each candidate is represented using key-value pairs:

```text
"name" → "Harsh"
"class" → "CSE"
"rollno" → 20
"subject" → "COA"
"cgpa_status" → "Pass"
```

---

## 🖥️ Sample Output

```text
Enter the candidate name: Harsh

Candidate Found!
Name: Harsh
Class: CSE
Roll No: 20
Subject: COA
CGPA Status: Pass
```

If the candidate does not exist:

```text
Enter the candidate name: Rahul

Candidate not found.
```

---

## 🧠 What I Learned

Through this task, I learned:

* What JSON is.
* Difference between JSON and a Python dictionary.
* How to read JSON files using `json.load()`.
* How JSON data becomes Python lists and dictionaries.
* How to search structured data.
* How to access dictionary values using keys.
* Why `with open()` is useful for file handling.
* How to perform case-insensitive searching.

---

## 🎤 Interview Questions & Answers

### 1. What is JSON?

**Answer:**

> JSON stands for JavaScript Object Notation. It is a lightweight data format used to store and exchange structured data. It is commonly used for communication between frontend and backend applications.

### 2. What is the difference between JSON and a Python dictionary?

**Answer:**

> A Python dictionary is a data structure used inside Python to store data in key-value pairs. JSON is a language-independent data format used to store and exchange structured data.

### 3. How do you read JSON from a file in Python?

**Answer:**

> We use `json.load()` to read JSON data from a file. We open the file using `with open()` and then use `json.load(file)` to convert the JSON data into Python objects such as a list or dictionary.

---

## 🔑 Important Difference

```text
json.load()  → Read JSON from a file
json.dump()  → Write JSON to a file
```

---

## 👨‍💻 Internship Information

**Internship:** Python Programming Internship
**Organization:** Veda Technology
**Task:** Day 21 — Create a JSON Data Processor
**Language:** Python

---

## ✅ Conclusion

The Day 21 project helped me understand how Python can process **structured JSON data**. I learned how to read JSON files, work with lists and dictionaries, search records, and display relevant information based on user input.
![alt text](<image.png>)


# Day 22 – File Organizer

## 📌 Project Overview

This project is a Python-based **File Organizer** that automatically scans a folder and organizes files into different folders according to their file extensions.

The main purpose of this project is to learn **filesystem automation using Python**.

---

## 🎯 Objective

* Learn how to work with files and folders using Python.
* Understand `pathlib`.
* Use `shutil` to move files.
* Automatically organize files based on their extensions.
* Handle duplicate filenames safely.
* Practice filesystem automation.

---

## 🛠️ Technologies Used

* Python
* `pathlib`
* `shutil`

---

## 📂 Project Structure

```text
day22/
│
├── program.py
├── file.py
├── image.jpg
├── node.csv
└── what.docx
```

The files are placed in the Day 22 folder for testing.

---

## ⚙️ How It Works

The program follows these steps:

1. Define the source directory using `Path(".")`.
2. `Path(".")` represents the current working directory.
3. Check whether the source directory exists.
4. Scan the directory using `iterdir()`.
5. Check whether each item is a file using `is_file()`.
6. Get the file extension using `suffix`.
7. Match the extension with a predefined category.
8. Create the required destination folder.
9. Check whether a file with the same name already exists.
10. Move the file using `shutil.move()`.
11. Display the result in the terminal.

---

## 🔑 Important Concepts

### 1. pathlib

`pathlib` is a Python module used for working with files and directories.

Example:

```python
from pathlib import Path

source_folder = Path(".")
```

The `.` represents the **current working directory**.

---

### 2. shutil

`shutil` provides high-level operations for working with files and directories.

In this project, it is used to move files:

```python
shutil.move(str(file), str(destination))
```

---

### 3. File Extension

The file extension is obtained using:

```python
extension = file.suffix.lower()
```

For example:

```text
image.jpg → .jpg
node.csv → .csv
what.docx → .docx
```

The extension is then used to determine the appropriate category.

---

### 4. Creating Folders

The program creates a destination folder when required:

```python
destination_folder.mkdir(exist_ok=True)
```

`exist_ok=True` prevents an error if the folder already exists.

---

### 5. Duplicate File Handling

Before moving a file, the program checks whether a file with the same name already exists:

```python
if destination.exists():
    print(f"Skipped duplicate file: {file.name}")
    continue
```

This prevents the existing file from being accidentally overwritten.

---

## 📊 Before and After

### Before

```text
day22/
├── program.py
├── file.py
├── image.jpg
├── node.csv
└── what.docx
```

### After

Depending on the extension categories defined in the program, the files are automatically moved into folders such as:

```text
day22/
├── program.py
├── Python/
│   └── file.py
├── Images/
│   └── image.jpg
├── Data/
│   └── node.csv
└── Documents/
    └── what.docx
```

---

## 🧪 Testing

A separate test folder or files created specifically for testing should be used whenever possible.

Important files should **not** be used for testing because the program moves files automatically.

---

## 💡 Key Learning

This project demonstrates how Python can automate repetitive file-management tasks.

Instead of manually creating folders and moving every file, Python can:

**Scan → Identify → Categorize → Create Folder → Move**

---

## 🎤 Interview Questions & Answers

### Q1. What is pathlib?

`pathlib` is a Python standard-library module that provides an object-oriented way to work with filesystem paths, files, and directories.

---

### Q2. What is the difference between os and shutil?

`os` provides functions for interacting with the operating system, including working with directories, paths, and environment information.

`shutil` provides higher-level operations for files and directories, such as copying and moving files.

---

### Q3. How can Python automate repetitive file-management tasks?

Python can use modules such as `pathlib`, `os`, and `shutil` to automatically scan directories, identify files, create folders, copy or move files, and organize them according to rules.

---

### Q4. What does `Path(".")` mean?

`Path(".")` represents the **current working directory** from which the Python program is being executed.

---

### Q5. What does `file.suffix` do?

`file.suffix` returns the extension of a file.

For example:

```python
Path("image.jpg").suffix
```

returns:

```text
.jpg
```

---

### Q6. Why is `is_file()` used?

`is_file()` checks whether a path represents a file. It helps prevent the program from trying to process directories as files.

---

## ✅ Conclusion

Day 22 helped me understand **filesystem automation in Python**.

I learned how to use `pathlib` to work with directories and file paths and `shutil` to move files automatically. This project shows how Python can reduce repetitive manual file-management work.

# 🎟️ Expense Tracker

## 📌 Project Overview

**Expense Tracker** is a Python-based ticket billing application that calculates the total expense for people purchasing tickets from a ticket counter.

The application provides different ticket categories — **Premium, Gold, and Silver** — and calculates the final payable amount based on:

* Ticket category
* Number of tickets
* Ticket price
* Applicable discount
* Cold drink charges
* Taxes

The project demonstrates how Python can be used to build a simple real-world billing and expense calculation system.

---

## 🎯 Objectives

The main objectives of this project are:

* To calculate ticket expenses automatically.
* To provide different ticket categories.
* To apply discounts according to the ticket category or purchase.
* To add additional charges such as cold drinks.
* To calculate applicable taxes.
* To generate the final payable amount.
* To practice Python variables, conditions, functions, and arithmetic operations.

---

## 🎫 Ticket Categories

The ticket counter provides three types of tickets:

| Category    | Description                                   |
| ----------- | --------------------------------------------- |
| **Premium** | Highest-level ticket with premium pricing     |
| **Gold**    | Mid-level ticket                              |
| **Silver**  | Basic ticket with comparatively lower pricing |

The user selects a ticket category and enters the required number of tickets.

---

## 💰 Expense Calculation

The basic calculation flow is:

```text
Ticket Price
     ↓
Number of Tickets
     ↓
Subtotal
     ↓
Discount
     ↓
Cold Drink Charges
     ↓
Taxes
     ↓
Final Amount
```

### Formula

```text
Subtotal = Ticket Price × Number of Tickets

Discounted Amount = Subtotal − Discount

Amount with Extras = Discounted Amount + Cold Drink Charges

Final Amount = Amount with Extras + Taxes
```

---

## 🥤 Additional Charges

Customers can also purchase cold drinks along with their tickets.

The cold drink expense is added to the ticket expense before calculating the final bill.

---

## 🧾 Taxes

Applicable taxes are calculated on the bill according to the logic implemented in the Python program.

The tax amount is then added to the customer's total expense.

---

## 🛠️ Technologies Used

* **Python 3**
* Conditional Statements
* Variables
* Arithmetic Operators
* Functions
* User Input
* Basic Billing Logic

---

## ▶️ How to Run

### 1. Clone or download the project

Open the project folder in VS Code or any Python-supported IDE.

### 2. Run the Python file

```bash
python expense_tracker.py
```

### 3. Enter the required details

The program will ask for information such as:

```text
Ticket Category
Number of Tickets
Cold Drink Selection
```

The program then calculates the discount, additional charges, taxes, and final payable amount.

---

## 🧪 Example Workflow

```text
Customer
   ↓
Select Ticket Category
   ↓
Premium / Gold / Silver
   ↓
Enter Number of Tickets
   ↓
Calculate Ticket Cost
   ↓
Apply Discount
   ↓
Add Cold Drink Charges
   ↓
Calculate Taxes
   ↓
Display Final Expense
```

---

## 📚 Concepts Practiced

This project helped practice:

1. **Variables** — storing ticket prices, quantities, discounts, and charges.
2. **Input/Output** — taking customer information and displaying the bill.
3. **Conditional Statements** — selecting the appropriate ticket category and charges.
4. **Arithmetic Operations** — calculating totals, discounts, and taxes.
5. **Functions** — organizing different parts of the billing logic.
6. **Real-World Problem Solving** — converting a ticket-counter scenario into a Python program.

---

## 🚀 Future Improvements

The project can be extended by adding:

* Customer name and ID
* Multiple customers in one session
* Automatic receipt generation
* File-based expense records
* CSV/JSON storage
* Daily and monthly expense reports
* GUI interface
* Database integration

---

## 👨‍💻 Project Type

**Python Mini Project — Ticket Billing & Expense Tracking System**

---

## 🏁 Conclusion

The **Expense Tracker** project demonstrates a simple real-world ticket billing system using Python.

It combines ticket pricing, category selection, discounts, additional purchases, and taxes to calculate the **final amount payable by the customer**.

This project provides practical experience in converting a real-world billing problem into structured Python logic.
#####DAY -23 INTERNSHIP COMPLETED
# Day 24 – CLI Quiz Application

## 📌 Project Overview

The **CLI Quiz Application** is a command-line based quiz program developed using Python.

The application loads quiz questions from a separate JSON file, displays questions and multiple-choice options, accepts answers from the user, validates the input, calculates the score, and displays the final result.

This project was developed as part of my **Python Programming Internship at Veda Technology**.

---

## 🎯 Objective

The main objectives of this project are:

* Practice Python dictionaries and lists
* Work with JSON data
* Use loops and functions/application flow
* Read data from an external JSON file
* Handle user input
* Validate user answers
* Calculate scores and percentages
* Randomize question order
* Display a final quiz summary

---

## 🛠️ Technologies Used

* **Python**
* **JSON**
* **Command Line / Terminal**
* **VS Code**

### Python Modules Used

```python
json
random
```

---

## 📂 Project Structure

```text
day-24--folder/
│
├── quiz_application.py
├── questions.json
└── README.md
```

### File Description

| File                  | Purpose                                                 |
| --------------------- | ------------------------------------------------------- |
| `quiz_application.py` | Contains the main quiz application logic                |
| `questions.json`      | Stores the quiz questions, options, and correct answers |
| `README.md`           | Contains project documentation                          |

---

## 📄 JSON Data Structure

The questions are stored separately in `questions.json`.

Example:

```json
{
    "question": "What is the capital of India?",
    "options": [
        "A. Mumbai",
        "B. New Delhi",
        "C. Kolkata",
        "D. Chennai"
    ],
    "answer": "B"
}
```

The JSON file contains **10 questions**.

Separating the questions from the Python program makes the application easier to maintain and update.

---

## ⚙️ How the Application Works

### 1. Import Modules

The program imports the `json` and `random` modules.

```python
import json
import random
```

### 2. Load Questions

The program opens the JSON file and loads the data.

```python
with open("questions.json", "r") as file:
    questions = json.load(file)
```

The JSON data is converted into Python lists and dictionaries.

### 3. Randomize Questions

The question order is randomized using:

```python
random.shuffle(questions)
```

This makes the quiz different each time it runs.

### 4. Display Questions

The program loops through the questions:

```python
for number, question_data in enumerate(questions, start=1):
```

## 🖥️ Output

The following screenshot shows the CLI Quiz Application running successfully:

![Quiz Application Output](quiz.png)


Copy this entire block into your `README.md`:

````markdown
# Day 25 - Python Utility Module

## Project Overview

This project demonstrates how to create a reusable Python utility module containing commonly used functions for validation, formatting, calculations, and file utilities.

The main objective is to understand **modular programming and code reusability**.

## Project Structure

```text
day-25-folder/
│
├── utility.py
├── example.py
└── README.md
````

## Files Description

### utility.py

This is the reusable Python module. It contains functions for:

* Email validation
* Number validation
* Name formatting
* Currency formatting
* Average calculation
* Percentage calculation
* File existence checking
* Line counting

### example.py

This program imports functions from `utility.py` and demonstrates how they can be reused in another Python program.

## Functions

### 1. is_valid_email(email)

Checks whether an email contains basic valid characters such as `@` and `.`.

### 2. is_valid_number(value)

Checks whether a given value can be converted into a number.

### 3. format_name(name)

Removes unnecessary spaces and formats the name using title case.

### 4. format_currency(amount)

Formats a number as Indian currency with two decimal places.

### 5. calculate_average(numbers)

Calculates the average of a list of numbers.

### 6. calculate_percentage(obtained, total)

Calculates the percentage using obtained marks and total marks.

### 7. file_exists(filename)

Checks whether a specified file exists.

### 8. count_lines(filename)

Counts the number of lines in a text file.

## How to Run

Open the terminal inside the project folder and run:

```bash
python example.py
```

## Example Import

A function from the utility module can be imported into another Python program:

```python
from utility import calculate_average

marks = [80, 90, 70]

average = calculate_average(marks)

print(average)
```

## Concepts Learned

* Python Modules
* Python Packages
* Importing Functions
* Code Reusability
* Modular Programming
* Functions
* File Handling
* Exception Handling
* Documentation
* Single Responsibility Principle

# Interview Questions and Answers

## 1. What is the difference between a module and a package?

**Answer:**

A module consists of a single Python file, whereas a package consists of many modules.

## 2. Why is code reusability important?

**Answer:**

Code reusability is important because it reduces redundancy and saves time. It also helps reduce unnecessary repeated work in a project.

## 3. Name two kinds of things you can put inside a utility module.

**Answer:**

We can put reusable functions such as validation functions, formatting functions, calculation functions, and file utility functions inside a utility module.

For example:

* Validation functions
* Calculation functions

## Conclusion

This project demonstrates how reusable functions can be organized inside a Python module and imported into another program.

It provides practical experience with **modular programming, code reuse, functions, and file utilities**.

## Day 25 Status

**Core Task:** Completed
**Utility Module:** Completed
**Example Program:** Completed
**Interview:** Completed
**Documentation:** Completed

```
```
## Output

![Program Output](image.png)



# Day 26 — Date & Time Utility

## 📌 Project Overview

This project is a **Date & Time Utility** built using Python's `datetime` module.

The main purpose of this project is to learn practical date and time manipulation in Python.

## 🎯 Objective

* Understand the `datetime` module
* Convert date strings into datetime objects
* Calculate age
* Calculate differences between dates
* Work with formatted dates and times
* Validate date input
* Understand leap-year handling through the standard library

## 🛠️ Technologies Used

* Python
* `datetime` module

## ⚙️ Supported Operations

The utility supports at least four operations:

1. Calculate Age
2. Calculate Days Between Dates
3. Calculate Working Days
4. Display Formatted Date & Time

## 🧠 Concepts Learned

### `datetime.strptime()`

Used to convert a date string into a `datetime` object.

```python
date_of_birth = datetime.strptime(dob, "%d-%m-%Y")
```

### `datetime.now()`

Used to get the current date and time.

```python
current_date = datetime.now()
```

### Date Difference

Two datetime objects can be subtracted to calculate their difference.

```python
difference = date2 - date1
```

The result is a `timedelta` object.

```python
print(difference.days)
```

### `strftime()`

Used to format a datetime object into a readable string.

```python
date_of_birth.strftime("%d-%m-%Y")
```

## 🎂 Sample Calculation — Age

Example input:

```text
Enter the DOB in (DD-MM-YYYY): 23-09-2023
```

Example output:

```text
DATE OF BIRTH: 23-09-2023
CURRENT DATE: 18-09-2026
YOUR AGE: 2 years
```

## ⚠️ Input Validation

The program uses `try-except` to handle invalid date formats.

```python
try:
    date_of_birth = datetime.strptime(dob, "%d-%m-%Y")
except ValueError:
    print("Invalid date format!")
```

## 🎤 Interview Questions & Answers

### 1. What is the datetime module?

The `datetime` module is a standard Python module used to work with dates and times. It can be used to create, format, parse, and calculate dates and times.

### 2. How do you calculate the difference between two dates?

First, convert date strings into datetime objects using `datetime.strptime()`. Then subtract one date from the other. Python returns the result as a `timedelta` object, and `.days` can be used to get the difference in days.

### 3. Why should date calculations use standard libraries?

Standard libraries provide reliable and built-in functions for date and time calculations. They handle cases such as leap years and date differences better than manual calculations.

## ▶️ How to Run

Open the project folder in the terminal and run:

```bash
python date_time_utility.py
```

## ✅ Learning Outcome

By completing this task, I learned how to use Python's `datetime` module for practical date and time operations instead of manually calculating dates.
## 📸 Output

![Date & Time Utility Output](output.png)


Absolutely, Captain. 🫡🔥 Here is the **Day 27 `README.md`**, including the four interview questions and your corrected answers.

````markdown
# Day 27 - Build a Simple API Client

## 📌 Project Overview

This project demonstrates how to use Python to communicate with a public REST API, send HTTP requests, receive JSON responses, extract information, and handle errors.

For practice, different HTTP methods were tested using JSONPlaceholder, including GET, POST, PUT, PATCH, and DELETE.

---

## 🎯 Objective

- Understand the basics of REST APIs
- Learn how HTTP requests work
- Use Python's `requests` library
- Work with JSON responses
- Check HTTP status codes
- Understand GET, POST, PUT, PATCH, and DELETE
- Add basic error handling

---

## 🛠️ Tools Used

- Python
- Requests library
- JSON
- JSONPlaceholder Public REST API

---

## 🌐 HTTP Methods Practiced

### GET
Used to retrieve data from the server.

### POST
Used to send data to the server, usually to create a new resource.

### PUT
Used to completely update or replace an existing resource.

### PATCH
Used to partially update an existing resource.

### DELETE
Used to delete a resource.

---

## 🔄 How the API Client Works

```text
Python Program
      ↓
HTTP Request
      ↓
REST API Server
      ↓
HTTP Response
      ↓
Check Status Code
      ↓
Convert Response to JSON
      ↓
Extract Required Data
      ↓
Display Formatted Output
````

---

## 📊 HTTP Status Code 200

HTTP status code `200` means **OK**.

It indicates that the request was successfully received and processed by the server.

Example:

```python
print(response.status_code)
```

Output:

```text
200
```

---

## 🐍 Python HTTP Requests

Python can make HTTP requests using the `requests` library.

Example:

```python
import requests

response = requests.get(url)

print(response.status_code)
```

The response can also be converted into JSON:

```python
data = response.json()
print(data)
```

---

## 🛡️ Error Handling

The API client checks the response status and handles request-related errors.

Example:

```python
try:
    response = requests.get(url)
    response.raise_for_status()

except requests.exceptions.RequestException as error:
    print("Request failed:", error)
```

This helps prevent the program from crashing when a connection or HTTP request fails.

---

# 🎤 Interview Questions & Answers

## 1. What is a REST API?

**Answer:**

A REST API is an API that follows REST principles and allows different applications to communicate over HTTP. It commonly uses methods like GET, POST, PUT, PATCH, and DELETE to work with resources, usually using JSON for data.

---

## 2. What is HTTP status code 200?

**Answer:**

HTTP status code 200 means OK. It indicates that the request was successfully received and processed by the server.

---

## 3. What is the difference between GET and POST?

**Answer:**

GET is used to retrieve data from a server, while POST is used to send data to a server, usually to create a new resource.

### Simple way to remember:

```text
GET  → Retrieve data
POST → Create/send data
```

---

## 4. How does Python make HTTP requests?

**Answer:**

Python can make HTTP requests using the `requests` library. For example, we can use `requests.get()` to send a GET request and receive the server's response.

Example:

```python
import requests

response = requests.get(url)
print(response.status_code)
```

---

## ▶️ How to Run

1. Install the requests library:

```bash
pip install requests
```

2. Run the Python program:

```bash
python api_client.py
```

---

## ✅ Result

The project successfully demonstrated basic REST API consumption using Python.

The GET, POST, PUT, PATCH, and DELETE HTTP methods were practiced using JSONPlaceholder, and JSON responses and HTTP status codes were handled successfully.

---

## 📚 Key Learning

Through this project, I learned how Python communicates with REST APIs, how HTTP methods are used, how JSON responses are handled, and how status codes and request errors can be checked.

---

## 👨‍💻 Internship

**Veda Technology - Python Programming Internship**

**Day:** 27/45
**Level:** 1
**Task:** Build a Simple API Client

```
```

# 🌦️ Weather Data CLI

## 📌 Project Overview

The **Weather Data CLI** is a command-line application developed in Python that retrieves real-time weather information for a user-provided city using a weather API.

This project combines **API requests, JSON processing, functions, environment variables, and error handling** into a practical Python application.

---

## 🎯 Objective

* Retrieve weather information using an API.
* Accept a city name from the user.
* Process the API response in JSON format.
* Display useful weather information in a formatted CLI.
* Handle invalid cities and API/network errors.
* Keep API credentials outside the source code.

---

## 🛠️ Technologies Used

* **Python**
* **Requests**
* **Weather API**
* **JSON**
* **Environment Variables**

---

## ⚙️ Features

* 🌍 Search weather by city name
* 🌡️ Display temperature
* 🤒 Display feels-like temperature
* 💧 Display humidity
* 🌤️ Display weather condition
* 💨 Display wind speed
* 🔐 API key stored outside the source code
* ⚠️ Error handling for API and network problems

---

## 📂 Project Structure

```text
weather-data-cli/
│
├── weather_cli.py
├── .env
├── .gitignore
└── README.md
```

> Keep `.env` out of GitHub because it contains the API credential.

---

## 🚀 How to Run

### 1. Install the required library

```bash
pip install requests
```

### 2. Configure the API key

Store your weather API key in an environment variable instead of directly writing it inside the Python source code.

Example:

```text
OPENWEATHER_API_KEY=your_api_key
```

### 3. Run the application

```bash
python weather_cli.py
```

### 4. Enter a city

```text
Enter city name: Mathura
```

The application then retrieves and displays the weather information.

---

## 📊 Sample Output

```text
================================
       WEATHER INFORMATION
================================
City        : Mathura
Temperature : 31°C
Feels Like  : 34°C
Humidity    : 62%
Weather     : Clear sky
Wind Speed  : 3.2 m/s
================================
```

---

## ⚠️ Error Handling

The application handles common problems such as:

* Invalid city names
* `404` — City/resource not found
* `401` — Invalid API credentials
* `429` — API rate limit exceeded
* Network/connection errors
* Other unexpected API errors

---

## 🧠 Concepts Learned

Through this project, I practiced:

1. Making HTTP API requests using `requests`
2. Processing JSON responses
3. Using Python functions
4. Handling exceptions
5. Working with HTTP status codes
6. Using environment variables for credentials
7. Formatting CLI output
8. Building a practical API-based Python application

---

## 🎤 Interview Questions

### 1. How do APIs authenticate requests?

APIs commonly authenticate requests using methods such as **API keys, tokens, OAuth, or other authentication mechanisms**. In this project, an API key is used and stored outside the source code.

### 2. What happens when an API returns a 404?

A `404 Not Found` status means that the requested resource could not be found. In a weather application, this can happen when the provided city cannot be found by the API. The application should handle this response and show a user-friendly message.

### 3. How would you handle API rate limits?

I would detect the `429 Too Many Requests` response, avoid making unnecessary requests, and retry after an appropriate delay if the API provides a `Retry-After` value. I would also consider caching results and limiting unnecessary API calls.

---

## ✅ Deliverables Completed

* [x] Working Weather CLI
* [x] API Integration
* [x] JSON Processing
* [x] Formatted Weather Output
* [x] Error Handling
* [x] Secure API Credential Handling
* [x] Interview Questions

---

## 👨‍💻 Author

**Harsh Chauhan**

B.Tech CSE (AIML)

**Internship Project — Veda Technology**
day - 28 is completed.