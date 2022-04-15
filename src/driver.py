from typing import Tuple
import heapq

class Driver:
  def __init__(self, agent, game) -> None:
    self.agent = agent
    self.game = game
  
  def ai_move(self, depth) -> Tuple[int, int]:
    """Calculate ai move and returns the coordinates

    Args:
        depth (int): an integer specifying the depth of search

    Returns:
        Tuple[int, int]: The row, column coordinates of the move
    """
    all_moves = self.game.legal_moves(True)
    heap = []
    for move, row, col in all_moves:
      score = self.agent.get_score(move, depth)
      heapq.heappush(heap, (-score, (row, col)))
    return heapq.heappop(heap)[1]
  
  def human_move(self) -> Tuple[int, int]:
    """Prompt human to move and returns the coordinates

    Returns:
        Tuple[int, int]: The row, column coordinates of the move
    """
    row = int(input("Please enter row: "))
    col = int(input("Please enter column: "))
    return (row, col)
  
  def play(self, ai_first = True, ai_depth = 8) -> None:
    """Play out the game versus ai

    Args:
        ai_first (bool, optional): Is the ai first to play. Defaults to True.
    """
    if ai_first:
      while True:
        ai_decision = self.ai_move(ai_depth)
        self.game.set_marker(ai_decision[0], ai_decision[1], self.game.player_marker)
        print(self.game)
        if self.game.is_game_over():
          break

        human_decision = self.human_move()
        self.game.set_marker(human_decision[0], human_decision[1], self.game.opponent_marker)
        print(self.game)
        if self.game.is_game_over():
          break
      print("Game over!")
    else:
      while True:
        print(self.game)
        human_decision = self.human_move()
        self.game.set_marker(human_decision[0], human_decision[1], self.game.opponent_marker)
        print(self.game)
        if self.game.is_game_over():
          break

        ai_decision = self.ai_move(ai_depth)
        self.game.set_marker(ai_decision[0], ai_decision[1], self.game.player_marker)
        # print(self.game)
        if self.game.is_game_over():
          break
      print("Game over!")
