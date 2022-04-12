import game.tic_tac_toe as ttt
import agents.minimax as mm

game1 = ttt.TicTacToe()
game1.set_marker(0, 0, 'O')
game1.set_marker(1, 1, 'O')
game1.set_marker(2, 2, 'O')
moves = game1.legal_moves('X')
for move in moves:
  print(move, move.is_game_over(), move.winner)
