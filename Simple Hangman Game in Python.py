import random

def hangman_game():
    # Predefined list of words
    words = ["python", "hangman", "programming", "computer", "keyboard"]
    
    # Select a random word
    secret_word = random.choice(words).lower()
    guessed_letters = []
    attempts_left = 6
    word_progress = ["_"] * len(secret_word)
    
    print("Welcome to Hangman!")
    print(" ".join(word_progress))
    print(f"You have {attempts_left} incorrect attempts allowed.")
    
    while attempts_left > 0 and "_" in word_progress:
        guess = input("\nGuess a letter: ").lower()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
            
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
            
        guessed_letters.append(guess)
        
        if guess in secret_word:
            # Update word progress with correctly guessed letters
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    word_progress[i] = guess
            print("Correct!")
        else:
            attempts_left -= 1
            print(f"Wrong! You have {attempts_left} attempts left.")
        
        # Display current game state
        print("\n" + " ".join(word_progress))
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
    
    # Game over - check win/lose condition
    if "_" not in word_progress:
        print(f"\nCongratulations! You guessed the word: {secret_word}")
    else:
        print(f"\nGame over! The word was: {secret_word}")

# Start the game
hangman_game()