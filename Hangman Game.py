# Hangman game project no 03
#The Hangman game is a classic word-guessing game where a random word is chosen and shown
#as blanks, and the player guesses letters one by one; correct guesses reveal letters in the word,
#while wrong guesses reduce the number of lives until the player either guesses the whole
# word or loses by running out of lives.

import random

wlist = ["apple", "beautiful", "potato", "calculator", "functions"]
cword = random.choice(wlist)      # this is where the random word from wlist will be choosen and stored
lives = 6
print(cword)

display = []

for i in range(len(cword)) :  # loop for displaying _ spaces for words in the choosen word
    display += "_"
print(display)

game_over = False  # for ending of game
while not game_over :
    gletter = input("Guess a letter :").lower()

    for pos in range(len(cword)) :
        letter = cword[pos]
        if letter == gletter :
            display[pos] =gletter
    print(display)

    if gletter not in cword :
        lives -= 1
        print(f"The left lives is {lives}")
        if lives == 0 :
            game_over = True
            print("You loose!!!!!!.")

    if "_" not in display :
        game_over = True
        print("You win!!!!!!!!.")





