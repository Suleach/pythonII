# Write a game, where the user has to guess a word
import random

list_of_words = ['simple', 'list','of', 'words']
the_word = list_of_words[random.randint(0,3)]
game_over = False
board = list("*" * len(the_word))
it_was = []
points = [0,0,0]
turn = 1
baraban = [100,200,300,400,500, 600,700, 800, 900, 1000,"priz"]
prizes = [
    "Automobil",
    "Putyovka",
    "Gazonokosilka",
    "Cheese",
    "Tapochki"
]
while not game_over:
    spin = random.randint(0, 10)
    print("")
    print("------------------------------")
    print(f"Turn Player {turn}")
    print(f"Player 1: {points[1]} points")
    print(f"Player 2: {points[2]} points")
    print(f"Guess a word: {' '.join(board)}")

    if type(baraban[spin]) == str:
        print("Sector priz on baraban")
        priz = prizes[random.randint(0,4)]
        money = 1000
        money_list = [250, 500, 750, 1000, 2000 ,3000]
        get_prize = False
        cnt=0
        amount = random.randint(3,7)
        while not get_prize:
            print(f"I wanna give you {money}!")
            choice = str(input(" What you goona take?(p/m): "))
            if choice =="p":
                cnt += 1
                money += money_list[random.randint(0,5)]
                if cnt == amount:
                    print(f"Congratulations, your prize is {priz}.")
                    get_prize = True
            else:
                print(f"Congratulations, you win {money} dollars")
                get_prize = True                   
    else:
        bet = baraban[spin]
        print(f"Bet is {bet}")

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
                points[turn] += bet
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