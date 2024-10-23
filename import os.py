import os
from easy import EasyModeGame
from medium import main as run_medium_game
from hard import HardModeGame

def welcome_message():
    print("Welcome to Secure Coding Game!")

def choose_mode():
    print("Available modes:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    while True:
        choice = input("Choose mode (1/2/3): ").strip()
        if choice in ['1', '2', '3']:
            return choice
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

def run_game_mode(mode):
    if mode == '1':
        game = EasyModeGame("easy_mode_questions.txt")
        game.start_game()
        return game
    elif mode == '2':
        run_medium_game()
        return None  # Medium game does not return an object
    elif mode == '3':
        game = HardModeGame("hard_mode_questions.txt")
        game.start_game()
        return game
    else:
        raise ValueError("Invalid mode choice.")

def save_game_results(user_name, mode, game_instance):
    mode_name = {
        '1': 'Easy',
        '2': 'Medium',
        '3': 'Hard'
    }
    filename = f"{user_name}_{mode_name[mode]}_game_results.txt"
    with open(filename, 'w') as file:
        file.write(f"User Name: {user_name}\n")
        file.write(f"Chosen Mode: {mode_name[mode]}\n")

        if game_instance:
            if hasattr(game_instance, 'skipped_levels'):
                file.write(f"Skipped Levels: {len(game_instance.skipped_levels)}\n")

            if hasattr(game_instance, 'answered_levels'):
                file.write(f"Attempted Levels: {len(game_instance.answered_levels)}\n")

            if hasattr(game_instance, 'score'):
                file.write(f"Total Score: {game_instance.score}\n")
        # Additional logic to save incorrect answers with correct solutions if needed

def play_game():
    welcome_message()
    user_name = input("Enter your name: ").strip()  # Ask for the user's name once
    print(f"Hello {user_name}!")

    while True:
        mode = choose_mode()

        if mode in ['1', '3']:
            game_instance = run_game_mode(mode)
        else:
            run_game_mode(mode)
            game_instance = None  # Medium mode does not return an object

        # Prompt to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break

    print("Game session ended. Goodbye!")

if __name__ == "__main__":
    play_game()
