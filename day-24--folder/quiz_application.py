import json
import random


# Load questions from JSON file
with open("questions.json", "r") as file:
    questions = json.load(file)


# Check if questions are available
if not questions:
    print("No questions found!")
    exit()


# Randomize question order
random.shuffle(questions)


score = 0
total_questions = len(questions)


# Quiz heading
print("=" * 45)
print("        CLI QUIZ APPLICATION")
print("=" * 45)

print(f"\nTotal Questions: {total_questions}")
print("Enter A, B, C, or D to answer.\n")


# Ask each question
for number, question_data in enumerate(questions, start=1):

    print(f"Question {number}: {question_data['question']}")

    # Display options
    for option in question_data["options"]:
        print(option)

    # Get valid answer
    while True:
        user_answer = input("Your answer: ").strip().upper()

        if user_answer in ["A", "B", "C", "D"]:
            break
        else:
            print("Invalid answer! Please enter A, B, C, or D.")

    # Check the answer
    if user_answer == question_data["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! Correct answer: {question_data['answer']}")

    print("-" * 45)


# Calculate result
wrong_answers = total_questions - score
percentage = (score / total_questions) * 100


# Display final result
print("\n" + "=" * 45)
print("             QUIZ RESULT")
print("=" * 45)

print(f"Total Questions : {total_questions}")
print(f"Correct Answers : {score}")
print(f"Wrong Answers   : {wrong_answers}")
print(f"Score           : {score}/{total_questions}")
print(f"Percentage      : {percentage:.2f}%")


# Display performance message
if percentage >= 80:
    print("Result: Excellent!")
elif percentage >= 60:
    print("Result: Good Job!")
elif percentage >= 40:
    print("Result: Keep Practicing!")
else:
    print("Result: Need More Practice.")


print("=" * 45)