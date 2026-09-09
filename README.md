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



