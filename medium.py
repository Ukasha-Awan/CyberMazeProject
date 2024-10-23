import re

# Regular expressions for email and password validation
email_regex = r'^[a-zA-Z0-9.%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

def is_valid_email(email):
    """Checks if the email format is valid."""
    return bool(re.match(email_regex, email))

def is_valid_password(password):
    """Checks if the password format and length are valid."""
    return len(password) >= 8 and bool(re.match(password_regex, password))

def validate_username(username):
    """Checks if the username is valid."""
    return len(username) >= 6  # Example condition for username validation

def validate_security_answer(answer):
    """Validates the security answer."""
    if len(answer) < 8:
        return False, "Answer must be at least 8 characters long."

    has_letter = False
    has_number = False
    consecutive_special_chars = 0

    for char in answer:
        if char.isalpha():
            has_letter = True
        elif char.isdigit():
            has_number = True
        elif char in "!@#$%^&*()_+-={}[]|\:;\"'<>,.?/":
            consecutive_special_chars += 1
            if consecutive_special_chars > 2:
                return False, "Answer cannot have more than two consecutive special characters."
        else:
            return False, "Answer contains invalid characters."

    if not has_letter or not has_number:
        return False, "Answer must contain both letters and numbers."

    return True, "Answer is valid."

def is_answer_correct(user_answer, correct_answer):
    """Checks if the user's answer matches the correct answer or meets the 10% similarity criterion."""
    user_lower = user_answer.lower()
    correct_lower = correct_answer.lower()
    
    # Matching criteria for 10% similarity
    match_criteria = len(set(correct_lower).intersection(set(user_lower))) / len(correct_lower) >= 0.1
    
    return user_lower == correct_lower or match_criteria

def load_levels(filename):
    """Loads levels from a file and returns them as a list of dictionaries."""
    levels = []
    with open(filename, 'r') as file:
        level_data = file.read().strip().split('\n\n')
        for level_str in level_data:
            level = {}
            lines = level_str.strip().split('\n')
            for line in lines:
                if line.startswith('Level:'):
                    level['level'] = int(line.split(':')[1].strip())
                elif line.startswith('Question:'):
                    level['question'] = line.split(':')[1].strip()
                elif line.startswith('Correct Answer:'):
                    level['correct_answer'] = line.split(':')[1].strip()
            levels.append(level)
    return levels

def display_levels(levels):
    """Displays the list of levels without their descriptions."""
    print("Levels List:")
    for level in levels:
        print(f"Level {level['level']}")

def main():
    levels = load_levels('medium_mode_questions.txt')
    total_levels = len(levels)
    current_level = 0
    user_score = 0
    
    display_levels(levels)
    
    start_levels = input("Do you want to start the levels? (yes/no): ").strip().lower()
    if start_levels != 'yes':
        print("Game stopped.")
        return
    
    while current_level < total_levels:
        print(f"\nLevel {levels[current_level]['level']}")
        print(levels[current_level]['question'])
        
        answer_prompt = input("Do you want to answer it or skip it? (answer/skip): ").strip().lower()
        
        if answer_prompt == 'skip':
            print("Skipping to the next level...")
            current_level += 1
            continue
        
        answer = input("Enter your answer: ").strip()
        
        if current_level == 0:  # Level 1 specific validation
            email = answer.split()[0]
            password = answer.split()[1]
            if is_valid_email(email) and is_valid_password(password):
                print("Answer is correct!")
                user_score += 1
            else:
                print("Answer is incorrect. Please enter again.")
                continue
        elif current_level == 1:  # Level 2 specific validation
            valid = validate_username(answer)
            if valid:
                print("Answer is correct!")
                user_score += 1
            else:
                print("Answer is incorrect. Please enter again.")
                continue
        elif current_level == 2:  # Level 3 specific validation
            valid, message = validate_security_answer(answer)
            if valid:
                print(message)
                user_score += 1
            else:
                print(message)
                continue
        elif current_level == 3 or current_level == 9:  # Levels 4 and 10 specific validation
            valid = is_valid_password(answer)
            if valid:
                print("Answer is correct!")
                user_score += 1
            else:
                print("Answer is incorrect. Please enter again.")
                continue
        elif current_level == 7 or current_level == 8:  # Levels 8 and 9 specific validation
            if is_answer_correct(answer, levels[current_level]['correct_answer']):
                print("Answer is correct!")
                user_score += 1
            else:
                print("Answer is incorrect.")
        else:  # General validation for other levels
            if 'correct_answer' in levels[current_level]:
                if is_answer_correct(answer, levels[current_level]['correct_answer']):
                    print("Answer is correct!")
                    user_score += 1
                else:
                    print("Answer is incorrect.")
            else:
                print("No correct answer specified for this level. Moving to the next level...")
        
        # Display user score after each level
        print(f"Your score after level {current_level + 1}: {user_score}/{total_levels}")
        
        # Move to the next level
        current_level += 1
    
    print(f"\nGame Over! Your final score is {user_score}/{total_levels}.")

if __name__ == "__main__":
    main()
