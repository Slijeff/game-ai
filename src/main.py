import game.tic_tac_toe as ttt
import game.gomoku as gmk
import agents.minimax as mm
import driver

# game = ttt.TicTacToe()
# agent = mm.MinimaxAgent()
# Drive = driver.Driver(agent, game)

# Drive.play(ai_first = False)

if __name__ == "__main__":
  gomoku = gmk.Gomoku()
  gomoku.set_marker(0, 0, "X")
  gomoku.set_marker(1, 1, "X")
  gomoku.set_marker(2, 2, "X")
  gomoku.set_marker(3, 3, "X")
  gomoku.set_marker(4, 4, "X")
  print(gomoku)
  print(gomoku.is_game_over())
  print(gomoku.winner)