import game.tic_tac_toe as ttt
import agents.minimax as mm
import driver

game1 = ttt.TicTacToe()
agent = mm.MinimaxAgent()
Drive = driver.Driver(agent, game1)

Drive.play()
