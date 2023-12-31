from replit import clear
from hangman_art import stages, logo
from hangman_words import word_list
import random 

# opening logo
print(logo)

# general variables
end_of_game = False
lives = 6

# generating a random word

chosen_word = random.choice(word_list).lower()

# creating a new list to store "_" called display
display = []

# inserting "_" in a new list which is the same length with chosen_word
for letter in chosen_word: 
    display += "_"

# irritates the input function  until there is no "_" in display


while not end_of_game:

    # asking user input to guess a letter
    guess = input("Guess a letter: ").lower()

    clear()
  
    if guess in display:
        print(f"You have already entered letter {guess}")

    # if given input letter matches the letter(s) in chosen_word, should replace "_" with guessed letter in display
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess

    # if given input letter doesn't match the letter(s) of chosen_word, should decrease the lives by 1
    if guess not in chosen_word:
        lives -= 1
        print("This letter is not in the word")

    # printing out the result (a new list called display)    
    print(f"{' '.join(display)}")


    # checking the game is over or not
    if "_" not in display:
        end_of_game = True
        print("You win :)")
        print(stages[lives])
    else:
        if lives == 0:
            end_of_game = True
            print("You lose :(")
            print(f"The word is {chosen_word.upper()}")
        print(stages[lives])


