from games import *

def h1(state):
    bestO = 0
    bestX = 0
    if state.utility == 1:
        return state.utility * infinity
	if state.utility == -1:
		return -state.utility * infinity
    for x in legal_moves(state):

        (nVX, z1) = k_in_row(state.board, x, 'X',(0,1))
        (nHX, z2) = k_in_row(state.board, x, 'X',(1,0))
        (nDDX, z3) = k_in_row(state.board, x, 'X',(1,1))
        (nDIX, z4) = k_in_row(state.board, x, 'X',(1,-1))

        if (z1 or z2 or z3 or z4) >= 4:
            bestX = 50000
        elif (z1 or z2 or z3 or z4) == 3:
            bestX = 30000

        (nVO, z1) = k_in_row(state.board, x, 'O',(0,1))
        (nHO, z2) = k_in_row(state.board, x, 'O',(1,0))
        (nDDO, z3) = k_in_row(state.board, x, 'O',(1,1))
        (nDIO, z4) = k_in_row(state.board, x, 'O',(1,-1))

        if (z1 or z2 or z3 or z4) >= 4:
            bestO = 100000
        elif (z1 or z2 or z3 or z4) == 3:
            bestO = 60000

        totalO = nVO + nHO + nDDO + nDIO
        totalX = nVX + nHX + nDDX + nDIX

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
    while (board.get((x, y)) == None or board.get((x, y)) == player) and y > 0 and y < 7 and x > 0 and x < 8:
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
                     n += 50 * p
                     p -= 0.10
             x, y = x + delta_x, y + delta_y

    x, y = move
    p = 1
    while (board.get((x, y)) == None or board.get((x, y)) == player) and y > 0 and y < 7 and x > 0 and x < 8:
            if x == (x - delta_x):
                 if board.get((x, y)) == None:
                     n += 50 * p
                     p -= 0.10
                 if board.get((x, y)) == player:
                     z += 1
                     n += 500
            elif y == (y - delta_y):
                 if board.get((x, y)) == player:
                     z += 1
                     n += 500
                 elif board.get((x, y)) == None:
                     n += 50
            elif y != (y - delta_y) and x != (x - delta_x):
                 if board.get((x, y)) == player:
                     z += 1
                     n += 500
                 elif board.get((x, y)) == None:
                     n += 50 * p
                     p -= 0.10
            x, y = x - delta_x, y - delta_y
    return (n, z)