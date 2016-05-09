from games import *

def h1(state):
    bestX = 0
    bestO = 0
    legalMoves = legal_moves(state)
    for x in legalMoves:
        nOV = k_in_row(state.board, x, 'O',(0,1))
        nOH = k_in_row(state.board, x, 'O',(1,0))
        nODD = k_in_row(state.board, x, 'O',(1,1))
        nODI = k_in_row(state.board, x, 'O',(-1,1))
        nXV = k_in_row(state.board, x, 'X',(0,1))
        nXH = k_in_row(state.board, x, 'X',(1,0))
        nXDD = k_in_row(state.board, x, 'X',(1,1))
        nXDI = k_in_row(state.board, x, 'X',(-1,1))

        totalO = nOV + nOH + nODD + nODI
        totalX = nXV + nXH + nXDD + nXDI
        if totalO > bestO:
            bestO = totalO
        if totalX > bestX:
            bestX = totalX
    return bestX - bestO

def legal_moves(state):

    return [(x, y) for (x, y) in state.moves
            if y == 1 or (x, y-1) in state.board]

def k_in_row (board, move, player,(delta_x,delta_y)):
    x, y = move
    n = 0
    p = 1
    z = 0

    while (board.get((x, y)) == None or board.get((x, y)) == player) and y < 8 and x < 7:
        if board.get((x, y)) == player:
            z += 1
            n += 500
        elif board.get((x, y)) == None:
            n += 50
        x, y = x + delta_x, y + delta_y
		
    while (board.get((x, y)) == None or board.get((x, y)) == player) and y < 7 and x < 8:
         if x == (x + delta_x):
             if board.get((x, y)) == None:
                 n += 50 * p
                 p -= 0.10
         elif y == (y + delta_y):
             if board.get((x, y)) == player:
                    z += 1
                    n += 500
             elif board.get((x, y)) == None:
                 n += 50
         elif y != (y + delta_y) and x != (x + delta_x):
             if board.get((x, y)) == player:
                 z += 1
                 n += 500
             elif board.get((x, y)) == None:
                 n += 40 * p
                 p -= 0.15
         x, y = x + delta_x, y + delta_y
    x, y = move
    p = 1
    while (board.get((x, y)) == None or board.get((x, y)) == player) and y > 0 and x > 0:
         if x == (x - delta_x):
             if board.get((x, y)) == player:
                 z += 1
                 n += 500
         elif y == (y - delta_y):
             if board.get((x, y)) == player:
                 z += 1
                 n += 500
             elif board.get((x, y)) == None:
                 n += 50
         elif y != (y + delta_y) and x != (x + delta_x):
             if board.get((x, y)) == player:
                 z += 1
                 n += 500
             elif board.get((x, y)) == None:
                 n += 40 * p
                 p -= 0.15
         x, y = x - delta_x, y - delta_y
    if z == 3:
        n += 5000
    if z >= 4:
        return infinity
    return n