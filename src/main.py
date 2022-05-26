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
    Drive.play(ai_first=False, ai_depth=1)
    # gomoku.set_marker(0, 0, gomoku.player_marker)
    # gomoku.set_marker(1, 1, gomoku.player_marker)
    # gomoku.set_marker(2, 2, gomoku.player_marker)

    # print(gomoku)
    # print(gomoku._has_neighbor([9,1]))
