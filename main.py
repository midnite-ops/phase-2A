import random 

def play():
    options = ('rock', 'paper', 'scissors')
    
    player = input('Enter your guess: ')
    
    computer_move = random.choice(options)
    
    while player not in options:
        player = input('Enter your guess: ')
    
    if player == computer_move:
        print(f'You chose {player}, Computer chose {computer_move}, You win')
        
    elif player == 'rock'  and  computer_move == 'scissors':
        print(f'You chose {player}, Computer chose {computer_move}, You win')
    
    elif player == 'paper'  and  computer_move == 'rock':
        print(f'You chose {player}, Computer chose {computer_move}, You win')
    
    elif player == 'scissors'  and  computer_move == 'paper':
        print(f'You chose {player}, Computer chose {computer_move}, You win')
        
    else:
       print(f'You chose {player}, Computer chose {computer_move}, You lose')
        
    reset()

def reset():
    reset = input('Restart the game?: ')
    if reset == 'yes':
        play()
    else:
        print('Game over')
        
play()
