from IPython.display import clear_output

def display_board(board):
    print('\n'*100)
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

def player_input():
    '''
    OUTPUT = (player 1 marker, Player 2 marker)
    '''
    marker = ''
    
    while not (marker =='X' and marker == 'O'):
        marker = input('Player1: Choose X or O:').upper()

    if marker == 'X':
        return ('X','O')

    else:
        return ('O','X')

def place_marker(board,marker,position):
    board[position] = marker

def win_check(board,mark):
    #WIN TIC TAC TOE?

    #ALL ROWS AND CHECK TO SEE IF THEY ALL SHARE THE SAME MARKER?
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[7] == mark and board[8] == mark and board[9] == mark)
    #ALL COLUMNS, CHECK TO SEE IF MARKER MATCHES
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[9] == mark and board[6] == mark and board[3] == mark) 
    #2 DIAGONALS, CHECK TO SEE MATCH
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[9] == mark and board[5] == mark and board[1] == mark)) 

import random
def choose_first():
    flip = random.randint(0,1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board,position):
    return board[position] == ' '           

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False

    #Board is full if we return true 
    return True

def player_choice(board):

    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position:(1-9)'))

    return position

def replay():
    input("Play again? Enter YES or NO")

    return choice == 'YES'


# WHILE LOOP to keep running the game
print('Welcome to the Tic Tak Toe')

while True:
    #Play the game

    #set up everything up (BOARD, WHO WILL PLAY FIRST,CHOOSE MARKERS X,O)
    the_board = [' ']*10
    Player1_marker,Player2_marker = player_input()

    turn = choose_first()
    print(turn + 'Will go first')   

    play_game = input('Ready to play? y or n')

    if play_game == 'y'
        game_on = True
    else:
        game_on == False

    #GAME PLAY

    while game_on:
        if turn == 'Player 1':
            #show the board 
            display_board(the_board)
            #Choose a postion
            position = player_choice(the_board)
            #place the marker on the position
            place_marker(the_board,Player1_marker,position)
            #check if they won
            if win_check(the_board,Player1_marker):
                display_board(the_board)

                print('Player 1 has Won!!!!')
                game_on = False
            
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!!')
                    game_on = False
                else:
                    turn = 'Player 2'  
                
    #PLAYER ONE TURN 
        else:
             #show the board 
            display_board(the_board)
            #Choose a postion
            position = player_choice(the_board)
            #place the marker on the position
            place_marker(the_board,Player2_marker,position)
            #check if they won
            if win_check(the_board,Player2_marker):
                display_board(the_board)

                print('Player 2 has Won!!!!')
                game_on = False
            
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!!')
                    game_on = False
                else:
                    turn = 'Player 1'  
                

    if not replay(): 
        break
# BREAK OUT OF THE LOOP ON replay()