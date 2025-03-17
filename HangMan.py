import random
from hangman_words import word_list
from hangman_art import stages ,logo

#  variable 'lives' to keep track of the number of lives left.
#  Set 'lives' to equal 6 because og 6 lifes

lives = 6

print (logo)
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    
    print("****************************<???>/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    

    display = ""
    if guess in correct_letters:
        print("you have already entered the letter, please enter a another letter")

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"


    print("Word to guess: " + display)


    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life")

    if guess not in chosen_word:
        lives -= 1

        if lives == 0:
            game_over = True

           
            print(f"***********************YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    
    print(stages[lives])
    