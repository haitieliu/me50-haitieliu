"""
Tic Tac Toe Player
"""

from audioop import minmax
from copy import deepcopy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    #IF THERE IS MORE X, then X's turn, if there is mroe O then O's turn
    # If they are equal, then X first then O

    X_turn=0
    O_turn=0

    for x in board:
        for y in x:
            if y == X:
                X_turn=X_turn+1
            elif y == O:
                O_turn = O_turn+1
    
    if X_turn > O_turn:
        return O
    
    return X
    
    
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    action = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                action.add((i, j))
    return action




def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i,j= action
    new_board = deepcopy(board)
    whosturn = player(board)

    if board[i][j] !=None :
        raise NameError('Not Valid')
    else:   
        new_board[i][j] = whosturn
        return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == X  and board[0][1] == X and board[0][2] == X:
        return X
    elif board[0][0] == O  and board[0][1] == O and board[0][2] == O:
        return O
    elif board[0][0] == X  and board[1][0] == X and board[2][0] == X:
        return X
    elif board[0][0] == O  and board[1][0] == O and board[2][0] == O:
        return O 
    elif board[0][0] == X  and board[1][0] == X and board[2][0] == X:
        return X
    elif board[0][0] == O  and board[1][0] == O and board[2][0] == O:
        return O 
    elif board[2][0] == X  and board[2][1] == X and board[2][2] == X:
        return X
    elif board[2][0] == O  and board[2][1] == O and board[2][2] == O:
        return O 
    elif board[0][2] == X  and board[1][2] == X and board[2][2] == X:
        return X
    elif board[0][2] == O  and board[1][2] == O and board[2][2] == O:
        return O 
    elif board[2][0] == X  and board[1][1] == X and board[0][2] == X:
        return X
    elif board[2][0] == O  and board[1][1] == O and board[0][2] == O:
        return O 
    elif board[0][0] == X  and board[1][1] == X and board[2][2] == X:
        return X
    elif board[0][0] == O  and board[1][1] == O and board[2][2] == O:
        return O
    elif board[0][1] == X  and board[1][1] == X and board[2][1] == X:
        return X
    elif board[0][1] == O  and board[1][1] == O and board[2][1] == O:
        return O
    elif board[1][0] == X  and board[1][1] == X and board[1][2] == X:
        return X
    elif board[1][0] == O  and board[1][1] == O and board[1][2] == O:
        return O
    else:
        return None


    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    
    for row in board:
        for cell in row:
            if cell is None:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    winner_player = winner(board)
    if winner_player == X:
        return 1
    elif winner_player == O:
        return -1
    else:
        return 0

            

    raise NotImplementedError

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    _, best_action = evaluation(board)
    return best_action


def evaluation(board):
    """
    Returns the optimal value and action for the current player on the board.
    """
    if terminal(board):
        return utility(board), None

    if player(board) == X:
        max_val = -math.inf
        best_action = None
        for action in actions(board):
            val, _ = evaluation(result(board, action))
            if val > max_val:
                max_val = val
                best_action = action
        return max_val, best_action
    else:
        min_val = math.inf
        best_action = None
        for action in actions(board):
            val, _ = evaluation(result(board, action))
            if val < min_val:
                min_val = val
                best_action = action
        return min_val, best_action





