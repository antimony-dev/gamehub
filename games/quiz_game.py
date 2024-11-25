def play():
    questions = [
        {"question": "What is the capital of France?", "answer": "paris"},
        {"question": "What is 2 + 2?", "answer": "4"},
        {"question": "Who wrote '1984'?", "answer": "george orwell"},
        {"question": "What is the color of the sky?", "answer": "blue"}
    ]
    
    score = 0
    for q in questions:
        print(f"Question: {q['question']}")
        answer = input("Your answer: ").lower()
        if answer == q["answer"]:
            score += 1
            print("Correct!")
        else:
            print(f"Wrong! The correct answer was '{q['answer']}'")
    
    print(f"\nYou got {score}/{len(questions)} correct.")
