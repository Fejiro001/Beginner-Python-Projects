import random
#play rock, paper, scissors with computer
#rules of the game
#r > s, s > p, p > r

#main function
def play():
    user = input("What is your choice? 'r' for rock, 'p' for paper, 's'for scissors: ")
    computer = random.choice(['r', 'p', 's'])
    #A tie
    if user == computer:
        return 'tie'
    #User wins
    if you_win(user, computer):
        return 'You won!'
    #Computer wins
    return 'You lost!' 

#Function that decides if user wins
def you_win(player, opponent):
    #true if player wins
    if(player == 'r' and opponent == 's') \
        or (player == 's' and opponent == 'p') or \
        (player == 'p' and opponent == 'r'):
        return True

print(play())