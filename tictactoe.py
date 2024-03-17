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
    x = numPieces(board)
    xsum = x[0]
    osum = x[1]

    return X if osum == xsum else O
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board. Also returns permutations of each set corresponding to winning condtions.
    This will always be constant. O(1) complexity
    """
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.append((i,j))

    return moves

def auxwin():
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
    winner = utility(board)
    if(winner==1):
        return X
    if(winner==-1):
        return O
    
    return None

def isFull(board):
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
    v = auxwin()[0] # vertical
    h = auxwin()[1] # horizontal
    d = auxwin()[2] # diagonal

    xsum = 0
    osum = 0

    vert = auxutility(board, v)
    if vert != 0: return -1 if vert == -1 else 1
    hor = auxutility(board, h)
    if hor != 0: return -1 if hor == -1 else 1
    diag = auxutility(board, d)
    if diag != 0: return -1 if diag == -1 else 1

    return 0 

""""
MINIMAX PART
_______________________                                 
"""  
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    boardcopy = copy.deepcopy(board)
    bestscore = -1000
    bestmove = (0,0)

    for a in actions(boardcopy):
        boardcopy[a[0]][a[1]] = player(boardcopy)
        score = Auxmm(boardcopy, 0, False)
        board[a[0]][a[1]] == EMPTY
        if score > bestscore:
            bestscore = score
            bestmove = (a[0],a[1])

    return (bestmove)

def Auxmm(board, depth, p):
    score = utility(board)
    #checking for winner
    if score != 0:
        return score
    if score == 1:
        return score - depth
    if score == -1:
        return score + depth
    #ismaximizing
    if p == True:
        bestscore = -1000
        for a in actions(board):
            print(actions(board))
            #is spot open
            board[a[0]][a[1]] = player(board)
            bestscore = max(bestscore, Auxmm(board, depth+1, False))
            board[a[0]][a[1]] = EMPTY
            #print(bestscore)
        return bestscore
    #isminimizing
    else:
        bestscore = 1000
        for a in actions(board):
            #is spot open
            board[a[0]][a[1]] = player(board)
            bestscore = min(bestscore, Auxmm(board, depth+1, True))
            board[a[0]][a[1]] = EMPTY
        return bestscore
