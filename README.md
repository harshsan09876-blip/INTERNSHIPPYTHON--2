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
