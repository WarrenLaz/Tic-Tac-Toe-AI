"""
Tic Tac Toe Player
"""

import math
import copy

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

def numPieces(board):
    # Calculates the number of X and O markers on the board
    xsum = 0
    osum = 0
    for column in board:
        for cell in column:
            if cell == 'X':
                xsum+=1
            elif cell == 'O':
                osum+=1

    return xsum, osum

def player(board):
    # Returns whether the current player is placing an X or O
    x = numPieces(board)
    xsum = x[0]
    osum = x[1]

    return X if osum == xsum else O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board. Also returns permutations of each set corresponding to winning condtions.
    This will always be constant.
    """
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.append((i,j))

    return moves

def result(board, action):
    """
    Returns the result of the board corresponding to the action
    """
    if(player(board) == X):
        board[action[0]][action[1]] = X
    else:
        board[action[0]][action[1]] = O
    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winner = utility(board)
    if(winner==1):
        return X
    if(winner==-1):
        return O   
    return None

def isFull(board):
    # Returns whether the board is full
    return (not(None in board[0]) and not(None in board[1]) and not(None in board[2]))

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if(isFull(board) or winner(board) != None):
        return True
    return False

def auxutility(board,sets):
    """
    Returns whether a 3 in a row has occured and the resulting score from the three in a row.
    """
    xsum = 0
    osum = 0

    for x in sets:
        for y in x:
            if(board[y[0]][y[1]] == X):
                xsum += 1
            if(board[y[0]][y[1]] == O):
                osum += 1

            if(xsum == 3):
                return 1
            if(osum == 3):
                return -1
        xsum = 0
        osum = 0
    return 0

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    auxwin = [[ [(0, 0), (0, 1), (0, 2)] , [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)] ], 
            [ [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)] , [(0, 2), (1, 2), (2, 2) ] ] ,
            [[(0,0), (1,1), (2,2)],[(0,2),(1,1), (2,0)]]]
    
    v = auxwin[0] # vertical
    h = auxwin[1] # horizontal
    d = auxwin[2] # diagonal

    check = auxutility(board, v)
    if check != 0: return -1 if check == -1 else 1
    check = auxutility(board, h)
    if check != 0: return -1 if check == -1 else 1
    check = auxutility(board, d)
    if check != 0: return -1 if check == -1 else 1

    return 0 

""""
MINIMAX PART
_______________________                                 
"""  
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    #see whos playing
    bestmove = value(board)
    #bestmove = [0,0]
    return bestmove[1]


def value(board):
    # Calculates the value of the board by iterating through all poaaible game states
    who = player(board)
    if terminal(board) == True:
        return utility(board),None
    # maximizing
    if who == X:
        v = -9999
        for a in actions(board):
            board[a[0]][a[1]] = player(board)
            v2 = value(board)
            board[a[0]][a[1]] = EMPTY
            if v2[0] > v:
                v = v2[0]
                bestmove = a
        return v,bestmove

    # minimizing
    if who == O:
        v = 9999
        for a in actions(board):
            board[a[0]][a[1]] = player(board)
            v2 = value(board)
            board[a[0]][a[1]] = EMPTY
            if v2[0] < v:
                v = v2[0]
                bestmove = a 
        return v,bestmove
