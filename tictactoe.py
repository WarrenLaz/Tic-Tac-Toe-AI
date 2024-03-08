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


def player(board):
    xsum = 0
    osum = 0
    for column in board:
        for cell in column:
            if cell == 'X':
                xsum+=1
            elif cell == 'O':
                osum+=1

    return X if osum == xsum else O


def actions():
    """
    Returns set of all possible actions (i, j) available on the board. Also returns permutations of each set corresponding to winning condtions.
    This will always be constant. O(1) complexity
    """
    return [[ [(0, 0), (0, 1), (0, 2)] , [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)] ], 
            [ [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)] , [(0, 2), (1, 2), (2, 2) ] ] ,
            [[(0,0), (1,1), (2,2)],[(0,2),(1,1), (2,0)]]]



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
    if( utility(board)==1):
        return X
    elif(utility(board)==-1):
        return O
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if(winner(board)==0):
        return True
    
    return False

def auxutility(board,sets):
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
            elif(osum == 3):
                return -1
        xsum = 0
        osum = 0
    return 0

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    v = actions()[0] # vertical
    h = actions()[1] # horizontal
    d = actions()[2] # diagonal

    xsum = 0
    osum = 0

    vert = auxutility(board, v)
    if vert != 0: return 1 if vert == 1 else -1
    hor = auxutility(board, h)
    if hor != 0: return 1 if vert == 1 else -1
    diag = auxutility(board, d)
    if diag != 0: return 1 if vert == 1 else -1

    return 0 


            

def minaux(board):
    return 1
def maxaux(board):
    return 1

def createtree(board):
    return board


def minimax(board):
    boardcop = copy.deepcopy(board)

    createtree(boardcop)
    """
    Returns the optimal action for the current player on the board.
    """

print(utility(
            [[X, O, O],
            [O, O, X],
            [O, X, X]]
))