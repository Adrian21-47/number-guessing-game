class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def run_quiz(self):
        for question in self.questions:
            print(question['question'])
            user_answer = input("Your answer: ")

            if user_answer.lower() == question['answer'].lower():
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Incorrect. The correct answer is {question['answer']}.\n")

        print("Quiz completed!")
        print(f"Your final score is: {self.score} out of {len(self.questions)}.")

if __name__ == "__main__":
    # Define your quiz questions
    quiz_questions = [
        {'question': 'What is the capital of France?', 'answer': 'Paris'},
        {'question': 'How many continents are there?', 'answer': '7'},
        {'question': 'What is the capital of Japan?', 'answer': 'Tokyo'},
        {'question': 'What was is name of the left winger of Real Madrid', 'answer': 'Vinicius'}
    ]

    # Create a Quiz instance and run the quiz
    my_quiz = Quiz(quiz_questions)
    my_quiz.run_quiz()
