from games import *

def h1(state):
    bestX = 0
    bestO = 0
    moveUses = legal_moves(state)
    for x in moveUses:
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
        if len(state.moves) == 0:
            print('terminal')
            return infinity
    return bestX - bestO

def legal_moves(state):

    return [(x, y) for (x, y) in state.moves
            if y == 1 or (x, y-1) in state.board]

def k_in_row (board, move, player,(delta_x,delta_y)):
    x_inicial, y_inicial = move
    x, y = move
    n = 0
    z = 0
    while (board.get((x, y)) == None or board.get((x, y)) == player) and y < 8 and x < 7:
        if board.get((x, y)) == player:
            z += 1
            n += 500
        elif board.get((x, y)) == None:
            n += 50 * funcionPos((x,y),(x_inicial,y_inicial))
        x, y = x + delta_x, y + delta_y

    x, y = move

    while (board.get((x, y)) == None or board.get((x, y)) == player) and y > 0 and x > 0:
        if board.get((x, y)) == player:
            z += 1
            n += 500
        elif board.get((x, y)) == None:
            n += 50 * funcionPos((x,y),(x_inicial,y_inicial))
        x, y = x - delta_x, y - delta_y
    if z >= 3:
        n += 5000
    return n

def funcionPos(move, inicial):
    x ,y = move
    x_inicial, y_inicial = inicial
    if (x-x_inicial == 0 and y-y_inicial == 1):
        return 0.7
    elif (x-x_inicial == 0 and y-y_inicial == 2):
        return 0.5
    elif (x-x_inicial == 0 and y-y_inicial == 3):
        return 0.3
    elif (x-x_inicial == 0 and y-y_inicial == -1):
        return 0.7
    elif (x-x_inicial == 0 and y-y_inicial == -2):
        return 0.5
    elif (x-x_inicial == 0 and y-y_inicial == -3):
        return 0.3
    elif (x-x_inicial == 1 and y-y_inicial == 1):
        return 0.6
    elif (x-x_inicial == 2 and y-y_inicial == 2):
        return 0.3
    elif (x-x_inicial == 3 and y-y_inicial == 3):
        return 0.1
    elif (x-x_inicial == -1 and y-y_inicial == -1):
        return 0.6
    elif (x-x_inicial == -2 and y-y_inicial == -2):
        return 0.3
    elif (x-x_inicial == -3 and y-y_inicial == -3):
        return 0.1
    else:
        return 1