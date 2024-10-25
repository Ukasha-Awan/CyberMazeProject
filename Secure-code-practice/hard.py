import difflib

class HardModeGame:
    def __init__(self, questions_file):
        self.questions_file = questions_file
        self.questions = self.load_questions()
        self.score = 0
        self.current_level = 1

    def load_questions(self):
        questions = []
        with open(self.questions_file, 'r') as file:
            level_data = {}
            code_lines = []
            correct_answer_lines = []
            is_code = False
            is_correct_answer = False
            for line in file:
                line = line.rstrip()  # Using rstrip() to remove trailing whitespace, including newlines
                if line.startswith("Level:"):
                    if level_data:
                        level_data["code"] = "\n".join(code_lines)
                        level_data["correct_answer"] = "\n".join(correct_answer_lines)
                        questions.append(level_data)
                        level_data = {}
                        code_lines = []
                        correct_answer_lines = []
                        is_code = False
                        is_correct_answer = False
                    level_data["level"] = int(line.split(":")[1].strip())
                elif line.startswith("Question:"):
                    level_data["question"] = line.split(":", 1)[1].strip()
                elif line.startswith("Code:"):
                    is_code = True
                    is_correct_answer = False
                    code_lines.append(line.split(":", 1)[1].strip())
                elif line.startswith("Correct Answer:"):
                    is_code = False
                    is_correct_answer = True
                    correct_answer_lines.append(line.split(":", 1)[1].strip())
                elif is_code:
                    if line == "":
                        is_code = False
                        is_correct_answer = True
                    else:
                        code_lines.append(line)
                elif is_correct_answer:
                    correct_answer_lines.append(line)
            if level_data:
                level_data["code"] = "\n".join(code_lines)
                level_data["correct_answer"] = "\n".join(correct_answer_lines)
                questions.append(level_data)
        return questions

    def show_levels(self):
        print("Hard Mode Levels:")
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
            print("\nCode:\n" + question['code'])
            action = input("Do you want to answer it or skip it? (answer/skip): ").strip().lower()
            if action == 'answer':
                self.answer_question(question)
            elif action == 'skip':
                continue
        self.end_game()

    def answer_question(self, question):
        print("Enter your answer (end with a blank line):")
        user_answer_lines = []
        while True:
            line = input().strip()
            if line == "":
                break
            user_answer_lines.append(line)
        user_answer = "\n".join(user_answer_lines)
        correct_answer = question['correct_answer'].strip()
        similarity = difflib.SequenceMatcher(None, user_answer, correct_answer).ratio()
        if similarity >= 0.1:  # Allowing for 10% similarity
            print("Correct answer!")
            self.score += 1
        else:
            print(f"Incorrect answer! The correct answer is:\n{correct_answer}")
        print(f"Current score: {self.score}")

    def end_game(self):
        print(f"\nGame over! Your final score is: {self.score}")

if __name__ == "__main__":
    game = HardModeGame("hard_mode_questions.txt")
    game.start_game()
