# Write a game, where the user has to guess a word
import random

list_of_words = ['simple', 'list','of', 'words']
the_word = list_of_words[random.randint(0,5)]
game_over = False
board = list("*" * len(the_word))
it_was = []
points = [0,0,0]
turn = 1
while not game_over:
    print("")
    print("------------------------------")
    print(f"Turn Player {turn}")
    print(f"Player 1: {points[1]} points")
    print(f"Player 2: {points[2]} points")
    print(f"Guess a word: {' '.join(board)}")
    user_guess = input("Enter a word or a letter: ")
    user_guess = user_guess.lower()

    if len(user_guess) == 1:
        no_letter = 1
        if user_guess in it_was:
            print(f'Word {user_guess} was try another')
            continue
        for i in range(len(the_word)):
            if the_word[i] == user_guess:
                board[i] = user_guess
                no_letter = 0
                points[turn] += 10
        if no_letter:
            print(f'No letter {user_guess} in this word')
            if turn == 1:
                turn = 2
            elif turn == 2:
                turn = 1
        it_was.append(user_guess)
            
    else:
        if user_guess == the_word:
            print(f"Correct! Congratulations! Player {turn}")
            game_over = True
        else:
            print("Incorrect, think again.")


# if the letter is incorrect, show some message
# if the letter is already guessed, do not change anything
# randomly add some points if a letter is guessed
# Have a list of words, and randomly pick a word from a list

# Two players game. Player one's turn. Guess the word.