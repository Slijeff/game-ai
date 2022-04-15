import game.tic_tac_toe as ttt
import agents.minimax as mm

game1 = ttt.TicTacToe()
agent = mm.MinimaxAgent()
game1.set_marker(0, 0, 'O')
game1.set_marker(1, 1, 'X')
game1.set_marker(0, 1, 'O')
all_moves = game1.legal_moves(True)
for move in all_moves:
  print(move)
  # Test one move with both true and false, if both score are 1, we will choose that?
  print(agent.minimax(move, 10, False))
  # break
  # agent.minimax(move, 1, True)
