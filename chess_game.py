# Create an 8x8 grid with a chessboard pattern
grid = [[i+j if (i+j)%2 == 0 else " " for i in range(8)] for j in range(8)]

# Initialize a 2D array to keep track of the pieces on the board
board = [[" " for _ in range(8)] for _ in range(8)]

# Function to print the current game state
def print_board():
    for row in grid:
        print(" ".join(row))

# define the pieces
pieces = [
    ('pawn', 'white', (1, 1)),
    ('pawn', 'white', (1, 2)),
    # ... add remaining white pieces
    ('pawn', 'black', (6, 1)),
    ('pawn', 'black', (6, 2)),
    # ... add remaining black pieces
]  
# Create a Class for Pieces:
class Piece:
    def __init__(self, name, color, position, valid_moves):
        self.name = name
        self.color = color
        self.position = position
        self.valid_moves = valid_moves

    def __repr__(self):
        return f"{self.color[0]} {self.name}"
    
# Initialize the Chesboard:
def initialize_chessboard(pieces):
    chessboard = create_chessboard()
    for piece in pieces:
        row, col = piece[2]
        chessboard[row - 1][col - 1] = Piece(*piece)
    return chessboard

def display_board(chessboard):
    for row in chessboard:
        print(' '.join(str(square) for square in row))
        
def validate_move(chessboard, current_player, source, destination):
    # Implement the logic to validate the move
    pass
def play_game(chessboard):
    current_player = 'white'
    while True:
        display_board(chessboard)
        print(f"{current_player}'s turn")
        source = input("Enter the source position: ").strip()
        destination = input("Enter the destination position: ").strip()

        if validate_move(chessboard, current_player, source, destination):
            # Implement the logic to move the piece
            pass
        else:
            print("Invalid move. Please enter a valid move.")

        # Implement the logic to check if the game is over
