class MinimaxAgent:
  
  def minimax(self, board, depth, maximizingPlayer) -> int:
    """A minimax evaluation function that calculates the value of possible moves

    Args:
        board (Game): a game object that contains the current state of the game
        depth (int): the search depth
        maximizingPlayer (bool): whether or not the current player is the maximizing player

    Returns:
        int: a score for the current board
    """
    if depth == 0 or board.is_game_over():
      return board.evaluate()
    if maximizingPlayer:
      value = float('-inf')
      for move, _, _ in board.legal_moves(True):
        value = max(value, self.minimax(move, depth - 1, False))
      return value
    else:
      value = float('inf')
      for move, _, _ in board.legal_moves(False):
        value = min(value, self.minimax(move, depth - 1, True))
      return value
  
  def alphabeta(self, board, depth, alpha, beta, maximizingPlayer) -> int:
    """A minimax evaluation function that calculates the value of possible moves using alpha-beta pruning

    Args:
        board (Game): a game object that contains the current state of the game
        depth (int): the search depth
        alpha (int): the alpha value
        beta (int): the beta value
        maximizingPlayer (bool): whether or not the current player is the maximizing player

    Returns:
        int: a score for the current board
    """
    if depth == 0 or board.is_game_over():
      return board.evaluate()
    if maximizingPlayer:
      value = float('-inf')
      for move, _, _ in board.legal_moves(True):
        value = max(value, self.alphabeta(move, depth - 1, alpha, beta, False))
        alpha = max(alpha, value)
        if beta <= alpha:
          break
      return value
    else:
      value = float('inf')
      for move, _, _ in board.legal_moves(False):
        value = min(value, self.alphabeta(move, depth - 1, alpha, beta, True))
        beta = min(beta, value)
        if beta <= alpha:
          break
      return value
  
  def get_score(self, board, depth) -> int:
    """A wrapper for minimax algorithm that will be expose to driver, modify this to use pruning.

    Args:
        board (Game): A game object
        depth (int): an integer specifying the depth of search

    Returns:
        int: a score for the current board
    """
    # return self.minimax(board, depth, False)
    return self.alphabeta(board, depth, float('-inf'), float('inf'), False)
  
  
