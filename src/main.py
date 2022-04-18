import game.tic_tac_toe as ttt
import agents.minimax as mm
import driver

game = ttt.TicTacToe()
agent = mm.MinimaxAgent()
Drive = driver.Driver(agent, game)

Drive.play(ai_first = False)
