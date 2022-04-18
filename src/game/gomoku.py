from __future__ import annotations
from typing import List, Tuple
from copy import deepcopy

class Gomoku:
  def __init__(self, board: List[List[str]] = None) -> None:
        """Initialize the board

        Args:
            board (List[List[str]], optional): The new board state to copy from, defaults to None.
        """
        self.player_marker = 'X'
        self.opponent_marker = 'O'
        self.empty_mark = '_'
        self.board = [[self.empty_mark] * 15 for _ in range(15)] if board is None else board
        self.winner = None