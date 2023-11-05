import random

def play():
    user = input("choice any 'r' for rock , 'p' for paper , 's' scssior : \n ")
    computer = random.choice(['r','p','s'])                    #now computers will choices the random choices

    if user == computer:
        return 'its a tie'
      
    if is_win(user , computer):
        return 'you win!'
    
    return'you lost!'

def is_win(player , opponent):    # this will returns true if the player wins

    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())
