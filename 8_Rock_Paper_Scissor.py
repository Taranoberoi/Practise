# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
#
# Remember the rules:
#     Rock beats scissors
#     Scissors beats paper
#     Paper beats rock
def rock_paper(Player1,Player2):
    if Player1 == 'Rock':
        if Player2 == 'scissors':
            print("Rock wins")
        else:
            print("Paper wins")
    elif Player1 == 'scissors':
        if Player2 == 'Paper':
            print("Scissor Wins")
        else:
            print("Rock Wins")
    elif Player1 == "Paper":
        if Player2 == "Rock":
            print("Paper wins")
        else:
            print("Scissor wins")







Player1 = input("Player 1 please enter the Value")
Player2 = input("Player 2 please enter the Value")

if Player1 == Player2:
    print("No one Wins")

else:
     rock_paper(Player1,Player2)





