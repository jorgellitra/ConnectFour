import games
from heurystica import *

player = raw_input("Introduzca primer jugador (X = Maquina, O = Persona): ")
difficulty = raw_input("Introduzca la dificultad de la partida (4 =  Facil, 5 = Media, 7 = Dificil): ")
game = games.ConnectFour(p=player)

state = game.initial

while True:
    print "Jugador a mover:", game.to_move(state)
    game.display(state)

    if player == 'O':
        col_str = raw_input("Movimiento: ")
        coor = int(str(col_str).strip())
        x = coor
        y = -1
        legal_moves = game.legal_moves(state)
        for lm in legal_moves:
            if lm[0] == x:
                y = lm[1]

        state = game.make_move((x, y), state)
        print("El jugador ha movido en: ", (x, y))
        player = 'X'
    else:
        print "Thinking..."
        #move = games.minimax_decision(state, game)
        #move = games.alphabeta_full_search(state, game)
        if difficulty == '4':
            move = games.alphabeta_search(state, game, d=4, eval_fn=h1)
        elif difficulty == '5':
            move = games.alphabeta_search(state, game, d=5, eval_fn=h1)
        elif difficulty == '7':
            move = games.alphabeta_search(state, game, d=7, eval_fn=h1)

        state = game.make_move(move, state)
        print("La maquina ha movido en: ", move)
        player = 'O'
    print "-------------------"
    if game.terminal_test(state):
        game.display(state)
        print "Final de la partida"
        break
