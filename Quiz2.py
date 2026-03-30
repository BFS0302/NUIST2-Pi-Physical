import time

def quiz_game():
    print("Welcome to Python Quiz")
    print("Answer with a/b/c/d/e only\n")

    questions = [
        "1. Which is NOT a Python data type?\na) int\nb) float\nc) rational\nd) string\ne) bool\n",
        "2. Which is NOT built-in function?\na) +\nb) %\nc) abs()\nd) sqrt()\n",
        "3. int + float will be:\na) int\nb) string\nc) error\nd) float\n",
        "4. Best multi-way decision:\na) if\nb) if-else\nc) if-elif-else\nd) try\n",
        "5. Which stops loop?\na) if\nb) exit\nc) continue\nd) break\n"
    ]

    answers = ["c", "d", "d", "c", "d"]
    score = 0

    for i in range(len(questions)):
        user_input = input(questions[i]).strip().lower()

        if user_input == answers[i]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

        time.sleep(0.5)
        print("------------------------------\n")

    print("Quiz completed!")
    print("Final score:", score, "/", len(questions))

quiz_game()
