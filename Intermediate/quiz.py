questions = [
    {
        "question": "What is the capital of Liberia?",
        "options": ["A) Berlin", "B) Madrid", "C) Monrovia", "D) Rome"],
        "correct_option": "C"
    },
    {
        "question": "What year did Liberia gain independence?",
        "options": ["A) 1847", "B) 1900", "C) 1776", "D) 1812"],
        "correct_option": "A"
    },
    {
        "question": "Which river is the longest in Liberia?",
        "options": ["A) Saint Paul River", "B) Cestos River", "C) Lofa River", "D) Cavalla River"],
        "correct_option": "A"
    },
    {
        "question": "What is the official language of Liberia?",
        "options": ["A) French", "B) English", "C) Spanish", "D) Portuguese"],
        "correct_option": "B"
    },
    {
        "question": "Which currency is used in Liberia?",
        "options": ["A) Liberian Dollar", "B) US Dollar", "C) Euro", "D) British Pound"],
        "correct_option": "A"
    }
]


score = 0

for i, q in enumerate(questions, start=1):

    print(f"\nQuestion {i}: {q['question']}")

    for option in q["options"]:

        print(option)
    
    answer = input("Enter your answer: ").strip().upper()
    
    if answer == q["correct_option"]:

        print("Correct!")

        score += 1

    else:

        print(f"Wrong! The correct answer was {q['correct_option']}.")


print(f"\nYour final score: {score}/{len(questions)}")