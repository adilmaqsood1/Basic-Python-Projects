import random

def guess(x):
    random_number = random.randint(1, x)

    guess = 0

    while guess != random_number:
        guess = int(input((f'please enter a number between 1 to {x}'))) 

        if guess > random_number:
            print('too high! try again')
        elif guess < random_number:
             print('number is too low')

    print('congrats! you have enter correct number')    

guess(10)        

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while guess != c:
        guess = random.randint(low, high)
        feedback = input((f' if {guess} is to high (h) ,too low (L) or correct (C)'))
        if feedback == 'h':
            high = guess -1
        elif feedback == 'L':
            low = guess + 1  

    print(f'congrats! you have enter correct number {guess}')    

guess(10)  



    

 