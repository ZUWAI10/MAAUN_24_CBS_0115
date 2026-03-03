# CLI Quiz Program

quiz = [
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Processing Unit", "B. Computer Personal Unit", "C. Central Print Unit", "D. Control Processing Unit"],
        "correct_answer": "A"
    },
    {
        "question": "Which programming language is used in this course?",
        "options": ["A. Java", "B. Python", "C. C++", "D. HTML"],
        "correct_answer": "B"
    },
    {
        "question": "What symbol is used for comments in Python?",
        "options": ["A. //", "B. /* */", "C. #", "D. --"],
        "correct_answer": "C"
    }
]

score = 0

for q in quiz:

    print("\n" + q["question"])

    for option in q["options"]:
        print(option)

    answer = input("Enter your answer (A/B/C/D): ")

    if answer.upper() == q["correct_answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

total_questions = len(quiz)
percentage = (score / total_questions) * 100

print("\nQuiz Completed!")
print("Score:", score, "/", total_questions)
print("Percentage:", percentage, "%")

if percentage >= 50:
    print("PASS")
else:
    print("FAIL")