# from player_logic import humanplayer, randomcomputerplayer

# class tictactoe:
#     def __init__(self):
#         self.board = ['' for _ in range(9)]
#         self.current_winner = None
    
#     def print_board(self):
#         for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
#             print('|' + '|'.join(row) + '|')

#     @staticmethod
#     def print_board_nums():
#         number_board = [[str(i) for i in range (j*3, (j+1)*3)] for j in range(3)]
#         for row in number_board:
#             print('|' + '|'.join(row) + '|')

#     def available_moves(self):
#         moves =[]
#         for (i, spot) in enumerate(self.board):
#             if spot == ' '  :
#                 moves.append(i)
#         return moves   
     
#     def empty_squares(self):
#         return ' ' in self.board
    
#     def num_empty_squares(self):
#         return self.board.count(' ')
    
#     def make_move(self, square, letter):
#         if self.board[square] == ' ':
#             self.board[square] = letter
#             if self.winner(square, letter):
#                 self.current_winner = letter
#             return True
#         return False
    
#     def winner(self, square, letter):
#         row_ind = square // 3
#         row = self.board[row_ind*3 : (row_ind + 1) * 3]
#         if all([spot == letter for spot in row]):
#             return True
        
#        # col_ind = square % 3
#        # column = [self.board[col_ind+i*3] for i in range(3)]
#         if all([spot == letter for spot in row]):
#             return True
        
#         if square % 2 == 0:
#             diagonal1 = [self.board[i] for i in [0, 4, 8]] 
#             if all([spot == letter for spot in diagonal1]):
#                 return True
#             diagonal2 = [self.board[i] for i in [2, 4, 6]]
#             if all([spot == letter for spot in diagonal2]):
#                 return True
#         return False
    
#     def empty_square(self):
#         return ' ' in self.board
    
# def play(game, x_player, o_player, print_game=True):    
#     if print_game:
#         game.print_board_nums()

#     letter = 'x'
#     while game.empty_square():
#         if letter =='0':
#             square = o_player.get_move(game)  

#         else:
#             square = x_player.get_move(game)               

#         if game.make_move(square, letter):
#             if print_game:
#                 print(letter + f'makes a move to {square}')
#                 game.print_board()
#                 print('')    

#             if game.current_winner:
#                 if print_game:
#                     print(letter + 'wins!')   
#                 return letter 

#             letter = 'o' if letter == 'x' else 'x'
#             # if letter == 'x':
#             #     letter = 'o'
#             # else:
#             #     letter = 'x'  
#         if print_game:
#             print('it\'s a tie')


# if __name__ == '__main__':
#     x_player = humanplayer('x')
#     o_player = randomcomputerplayer('o')
#     t = tictactoe()
#     play(t , x_player, o_player, print_game=True)

from player_logic import randomcomputerplayer
from rock_paper_scssiors import play

class humanplayer:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        valid_move = False
        while not valid_move:
            move = input(f'Player {self.letter}, enter your move (0-8): ')
            try:
                move = int(move)
                if move in game.available_moves():
                    valid_move = True
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 8.")
        return move

class tictactoe:
    # ... (the rest of your existing tictactoe class code)

 def play(game, x_player, o_player, print_game=True):    
    if print_game:
        game.print_board_nums()

    letter = 'x'
    while game.empty_squares():
        if letter == 'o':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to {square}')
                game.print_board()
                print('')    

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter 

            letter = 'o' if letter == 'x' else 'x'

    if print_game:
        print("It's a tie!")

if __name__ == '__main__':
    x_player = humanplayer('x')
    o_player = randomcomputerplayer('o')
    t = tictactoe()
    play(t, x_player, o_player, print_game=True)
