import json
import random

def load_questions():
    with open("questions.json", "r") as file:
        return json.load(file)
    
    def ask_questions(question_data, question_number):
        print(f"\nQuestion{question_number}: {question_data['question']}")
        
        for option in question_data["options"]:
            print(option)
            
        while True:
            answer = input("Enter your answer(A/B/C/D): :").strip().upper()
            
            
            if answer in ["A", "B", "C", "D"]:return answer
            
    print("Invalid answer. Please enter A, B, C, or D.")
    
    
    def run_quiz():
        questions = load_questions()
        
        random.shuffle(questions)
        
    score = 0
    print("=" * 40)
    print(" CLI QUIZ APPLICATION")
    print("=" * 40)
    
    
    for number, question in enumerate(questions, start=1):
        user_answer = ask_question(question, number)
        
        if user_answer == question["answer"]:
            print("correct! ")
            score += 1
            
        else:
            print(f"wrong! correct answer: {question['answer']}")
            
            total = len(questions)
            
            percentage = (score / total) * 100
            
            
            print( "\n" + "=" * 40)
            print(" Final Result")
            print("=" * 40)
            print(f"score : : {score}/{total}")
            print(f"Percentage: {Percentage:.2f}%")
            
            
            if percentage >= 80:
                print("Result : Excellent!")
            elif percentage >= 50:
                print("Result   :Good Effort!")
                
            else:
                print("Result  :Keep Practicing!")
                
            print("=" * 40)
            
            if __name__ == "__main__":
                run_quiz()