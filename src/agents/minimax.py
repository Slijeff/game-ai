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
      return self.eval_fn(board)
    if maximizingPlayer:
      value = float('-inf')
      for move in board.legal_moves():
        value = max(value, self.minimax(move, depth - 1, False))
      return value
    else:
      value = float('inf')
      for move in board.legal_moves():
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
      return self.eval_fn(board)
    if maximizingPlayer:
      value = float('-inf')
      for move in board.legal_moves():
        value = max(value, self.alphabeta(move, depth - 1, alpha, beta, False))
        alpha = max(alpha, value)
        if beta <= alpha:
          break
      return value
    else:
      value = float('inf')
      for move in board.legal_moves():
        value = min(value, self.alphabeta(move, depth - 1, alpha, beta, True))
        beta = min(beta, value)
        if beta <= alpha:
          break
      return value
  
  
