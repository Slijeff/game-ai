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
  agent = mm.MinimaxAgent()
  Drive = driver.Driver(agent, gomoku)
  Drive.play(ai_first = False, ai_depth=1)