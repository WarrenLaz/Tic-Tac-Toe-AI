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


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]



def result(board, action):
    if(player(board) == X):
        board[action[0]][action[1]] = X
    else:
        board[action[0]][action[1]] = O

    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if(utility(board)==1):
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


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    v = [ [(0, 0), (0, 1), (0, 2)] , [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)] ]
    h = [ [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)] , [(0, 2), (1, 2), (2, 2) ] ] 
    d = [[(0,0), (1,1), (2,2)],[(0,2),(1,1), (2,0)]]

    xsum = 0
    osum = 0
    for x in v:
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

    for x in h:
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

    for x in d:
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
            [[X, O, X],
            [O, X, X],
            [O, X, O]]
))