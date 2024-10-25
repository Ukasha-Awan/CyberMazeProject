
class EasyModeGame:
    def __init__(self, questions_file):
        self.questions_file = questions_file
        self.questions = self.load_questions()
        self.score = 0
        self.current_level = 1

    def load_questions(self):
        questions = []
        with open(self.questions_file, 'r') as file:
            level_data = {}
            for line in file:
                line = line.strip()
                if line.startswith("Level:"):
                    if level_data:
                        questions.append(level_data)
                        level_data = {}
                    level_data["level"] = int(line.split(":")[1].strip())
                elif line.startswith("Question:"):
                    level_data["question"] = line.split(":", 1)[1].strip()
                elif line.startswith("Option"):
                    option = line.split(")")[0] + ")"
                    text = line.split(")")[1].strip()
                    level_data[option] = text
                elif line.startswith("Correct Answer:"):
                    level_data["correct_answer"] = line.split(":", 1)[1].strip()
            if level_data:
                questions.append(level_data)
        return questions

    def show_levels(self):
        print("Easy Mode Levels:")
        for question in self.questions:
            print(f"Level {question['level']}")

    def start_game(self):
        self.show_levels()
        start = input("Do you want to start the levels? (yes/no): ").strip().lower()
        if start == 'yes':
            self.play_level()

    def play_level(self):
        for question in self.questions:
            self.current_level = question['level']
            print(f"\nLevel {self.current_level}")
            print(question['question'])
            for option in ["Option a)", "Option b)", "Option c)", "Option d)"]:
                if option in question:
                    print(f"{option} {question[option]}")
            action = input("Do you want to answer it or skip it? (answer/skip): ").strip().lower()
            if action == 'answer':
                self.answer_question(question)
            elif action == 'skip':
                continue
        self.end_game()

    def answer_question(self, question):
        user_answer = input("Enter your answer (a/b/c/d): ").strip().lower()
        correct_answer = question['correct_answer'].strip().split(')')[0][-1].lower()
        if user_answer == correct_answer:
            print("Correct answer!")
            self.score += 1
        else:
            print(f"Incorrect answer! The correct answer is: {question['correct_answer']}")
        print(f"Current score: {self.score}")

    def end_game(self):
        print(f"\nGame over! Your final score is: {self.score}")

if __name__ == "__main__":
    game = EasyModeGame("easy_mode_questions.txt")
    game.start_game()
