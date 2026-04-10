from services import question_generator
from services.question_generator import easy, medium, hard
from services.evaluate_question import evaluate_answer

# q = easy()

def run_quiz(question_data=None):


    # This list will store all questions and user answers for the final report
    quiz_history = []

    while True:
        choice = input("\nChoose a level (easy, medium, hard) or 'exit' to quit: ").lower().strip()
        # question_data = easy()


        if choice == "exit":
            break

        # 1. Generate the question
        if choice == "easy":
            question_data = easy()
        elif choice == "medium":
            question_data = medium()
        elif choice == "hard":
            question_data = hard()
        else:
            print("Invalid level. Please choose easy, medium, or hard.")
            continue
        #
        # # 2. Show the question
        # print("\n" + "=" * 40)
        # print(question_data)
        # print("=" * 40)

        # 3. Get the user's answer
        user_choice = input("Your Answer (A, B, C, or D): ").strip().upper()

        # 4. Save to history (we don't show the result yet!)
        quiz_history.append({
            "question": question_data,
            "user_answer": user_choice
        })
        print("✅ Answer recorded. Choose another level or type 'exit' for results.")




if __name__ == "__main__":
    print("--- 🎓 StudyBuddy: Data Science Quiz Mode ---")
    run_quiz()
    # print(q)