#QUIZ PROGRAM
questions = ("What is the capital of France?",
             "Which planet is known as the Red Planet?",
             "What is 5 + 3?",
             "Which animal is known as the King of the Jungle?",
             "What do plants need to make food?")
answers = ("D","C","B","C","B")
options = (("A. Berlin","B. Madrid","C. Rome","D. Paris"),
           ("A. Earth","B. Mars","C. Venus","D. Mercury"),
           ("A. 15","B. 8","C. 6","D. 7"),
           ("A. Crocodile","B. Elephant","C. Lion","D. Tiger"),
           ("A. Moonlight","B. Sunlight","C. Wind","D. Sound"))
question_num = 0
score = 0
guesses = []
for question in questions :
    print("-----------------------------")
    print(question)
    for option in options[question_num]:
        print(f"{option}")
    guess = input("Choose (A,B,C,D) : ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score +=1
        print("CORRECT ANSWER")
    else:
        print(f"{guess} is WRONG ANSWER")
        print(f"The correct answer is {answers[question_num]}")
    question_num += 1
print("---------------------")
print(f"Your score is {score}/5")