import random

# Load words from a file
def load_words(filename = 'C:\\Users\\Public\\Documents\\09CH6\\words.txt'):
    with open(filename, 'r') as file:
        words = file.read()
    return words

# Choose random letters
def choose_letters():
    alphabet = 'aeioubflmd'
    letters = random.sample(alphabet, 7)
    return letters

# Checking if a word can be formed from the given letters
def can_form_word(word, letters):
    letter_count = {}
    for letter in letters:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    for letter in word:
        if letter not in letter_count or letter_count[letter] == 0:
            return False
        else:
            letter_count[letter] -= 1
    return True

# Main loop
def word_builders_game():
    words = load_words('words(2).txt')
    letters = choose_letters()
    print("Welcome to Word Builders!")
    print("Letters: ", ' '.join(letters))
    
    chances = 3
    while chances > 0:
        user_input = input(f"Enter a three-letter word (or 'quit' to exit), {chances} chances left: ").lower()
        
        if user_input == 'quit':
            print("Thanks for playing!")
            return
        
        if user_input in words:
            if can_form_word(user_input, letters):
                print("Valid word! You win!")
                chances -=1
            else:
                print("Word cannot be formed from the given letters. Try again!")
                chances -= 1  
        else:
            print("Not a valid word. Try again!")
            chances -= 1

    print("You ran out of chances! You lose!")

# call function word_builders_game
word_builders_game()
