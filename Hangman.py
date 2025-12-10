import random

def play_game():
    # 1. Predefined words
    words = ["apple", "water", "chair", "tiger", "cloud"]

    # 2. Random word selection
    secret_word = random.choice(words)
    
    attempts = 6
    guesses = []
    
    print("Welcome to the Word Guessing Game!")
    print("I have chosen a word. Can you guess it?")
    
    # Game loop
    while attempts > 0:
        # 3. Display hidden word
        display_word = ""
        missing_letter = False
        for letter in secret_word:
            if letter in guesses:
                display_word += letter + " "
            else:
                display_word += "_ "
                missing_letter = True
        
        print(f"\nWord: {display_word.strip()}")
        print(f"Attempts left: {attempts}")
        
        # 6. Ending condition: Win
        if not missing_letter:
            print("\n✔️ You win!")
            return

        # 4. User guesses letters
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
            
        if guess in guesses:
            print("You already guessed that letter.")
            continue
            
        guesses.append(guess)
        
        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            # 5. Attempts limit: Reduce attempts
            attempts -= 1

    # 6. Ending condition: Lose
    print("\n❌ You lose!")
    print(f"The word was: {secret_word}")

if __name__ == "__main__":
    play_game()
