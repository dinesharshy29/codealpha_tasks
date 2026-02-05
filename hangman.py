import random

def hangman():
    words = ['python', 'programming', 'codealpha', 'internship', 'developer', 'algorithm', 'software', 'jupyter', 'github', 'automation']
    word = random.choice(words).lower()
    guessed_letters = []
    attempts = 6
    
    stages = [
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / \\
           |
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / 
           |
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |      
           |
        """,
        """
           --------
           |      |
           |      O
           |     /|
           |      
           |
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      
           |
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |
        """
    ]

    print("Welcome to Hangman!")
    
    while attempts > 0:
        print(stages[attempts])
        
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print(f"Word: {display_word}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Attempts left: {attempts}")
        
        if "_" not in display_word:
            print(f"Congratulations! You guessed the word: {word}")
            break
            
        guess = input("Enter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
            
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
            
        guessed_letters.append(guess)
        
        if guess not in word:
            attempts -= 1
            print(f"Wrong guess! '{guess}' is not in the word.")
            
    if attempts == 0:
        print(stages[0])
        print(f"Game Over! The word was: {word}")

if __name__ == "__main__":
    hangman()
