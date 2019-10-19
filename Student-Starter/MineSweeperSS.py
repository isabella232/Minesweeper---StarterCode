import random


class Cell(object):
    def __init__(self, is_mine, is_visible=False, is_flagged=False):
        ''' Set attributes to the class Cell
        Our attributes should tell us if it is visible, if its flagged, and if its visible'''

        ''' For every setter we use, to need to use a .self
            Create a function for every attribute for cell. 
            '''



class Board(tuple):
    def __init__(self, '__'):
        ''' Create attributes to assign to our board'''
    def mine_repr(self, row_id, col_id): ''' This function sets up a column'''
        cell = self[row_id][col_id]
        if cell.is_visible:
            ''' If the cell is a mine, indicate that. If the cell is not, tell the user the amount of nearby mines'''

        elif '______': #If Cell is Flagged, Indicate that

        else: #Indicate that the cell is not visible


    def __str__(self):
        board_string = ''' This string tells us how many mines are remaining '''
        for (row_id, row) in enumerate(self):
            board_string += ("\n" + str(row_id) + " " +
                             "".join(self.mine_repr(row_id, col_id) for (col_id, _) in enumerate(row)) +
                             " " + str(row_id))
        board_string += "\n  " + "".join([str(i) for i in range(len(self))])
        return board_string

    def show(self, row_id, col_id):
        ''' This function accounts for visible cells. If a mine cell is visible, but not flagged, the game is over
            However, this does not apply if the cell is flagged.
            If a non-cell mine is visible and all of its adjacent cells are not mines, we want to reveal all the
            adjacent cells'''
        cell = self[row_id][col_id]
        if not cell.is_visible:
            cell.show()
            ''' this if statement is to determine if the game ended'''
            if '...':
            ''' This if statement is to reveal all the surround cells a non-mine cell with no adjacent mine-cells'''
            elif '...':

    ''' This function is to allow the player to flag cells. We can only flag non-visible cells. If the player
        tries to flag a visible cell, display an error message'''
    def flag(self, row_id, col_id):
        cell = self[row_id][col_id]


    def place_mine('__', '__', '__'):
        ''' This function sets a mine in a cell in the grid'''

    def count_surrounding(self, row_id, col_id):
        ''' this function should return the number of surrounding mines near a cell. Add up the surrounding mines
        and display that number'''

    def get_neighbours(self, row_id, col_id):
        ''' This function counts the number of neighbors for a cell. A cell in the middle in the grid
         should have 8 neighbors'''
    def is_in_range(self, row_id, col_id):
        ''' This function should determine if the player inputs are within the range of the board.
            If the player chose column '-1', that input would be invalid. We need to account for that'''

    @property
    def remaining_mines(self):
        remaining = 0
        ''' This function checks every cell for mines. If there is a mine, +1 to mine count. If the cell is flagged
        , we -1 to the mine count. Return the remaining mines'''

    @property
    def is_solved(self):
        '''Return the solution to the board. Reveal all the cells and whether or not they are a mine'''

def create_board(size, mines):
    board = Board(tuple([tuple([Cell(False) for i in range(size)])
                         for j in range(size)]))
    available_pos = list(range((size - 1) * (size - 1)))
    for i in range(mines):
        new_pos = random.choice(available_pos)
        available_pos.remove(new_pos)
        (row_id, col_id) = (new_pos % 9, new_pos // 9)
        board.place_mine(row_id, col_id)
    return board

def get_move(board):
    INSTRUCTIONS = ("First, enter the column, followed by the row. To add or "
                    "remove a flag, add \"f\" after the row (for example, 64f "
                    "would place a flag on the 6th column, 4th row). Enter "
                    "your move: ")
    '''Ask the user to enter a move. Provide a special key for the player to press if they want to review the instructions '''
    move = '...'
    if '...':
    ''' create a while loop for when the player puts in an invalid input such -1 column or -1 row. Prompt them again
    for another input and give them the option to access the instructions again.'''


    return (int(move[1]), int(move[0]), move[-1] == "f")

def is_valid(move_input, board):
    ''' This function applies when the move is valid. '''
    if move_input == "H" or (len(move_input) not in (2, 3) or
                             not move_input[:1].isdigit() or
                             int(move_input[0]) not in range(len(board)) or
                             int(move_input[1]) not in range(len(board))):
        return False

    if len(move_input) == 3 and move_input[2] != "f":
        return False

    return True


def main():
    SIZE = ''' Determine the size of the board'''
    MINES = ''' Determine the number of mines'''
    board = create_board(SIZE, MINES)
    print(board)
    while board.is_playing and not board.is_solved:
        ''' While the game is playing and the board is not solved, we need to get a move from the player.
        If the player's move is a flag, we need to be aware of that'''

    if board.is_solved:
        ''' Congratulate then. If the board is not solved, the game is over and display a message saying that'''

main()