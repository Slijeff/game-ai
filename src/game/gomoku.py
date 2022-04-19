from __future__ import annotations
from typing import List, Tuple
from copy import deepcopy


class Gomoku:
    def __init__(self, board: List[List[str]] = None) -> None:
        """Initialize the board

        Args:
            board (List[List[str]], optional): The new board state to copy from, defaults to None.
        """
        self.board_size = 15
        self.player_marker = 'X'
        self.opponent_marker = 'O'
        self.empty_mark = '_'
        self.board = [[self.empty_mark] * self.board_size for _ in range(
            self.board_size)] if board is None else board
        self.winner = None

    def __repr__(self) -> str:
        """Return a string representation of the board

        Returns:
            str: string representation of the board
        """
        ret_str = ''
        for i in range(self.board_size):
            ret_str += f'  {i}'
        ret_str += '\n'
        for row in range(self.board_size):
            ret_str += f'{row}'
            for col in range(self.board_size):
                ret_str += f' {self.board[row][col]} '
            ret_str += '\n'
        return ret_str

    def set_marker(self, row: int, col: int, player: str) -> None:
        """Set the marker at the given position

        Args:
            row (int): row index
            col (int): column index
            player (str): player marker

        Returns:
            None
        """
        self.board[row][col] = player

    def is_game_over(self) -> bool:
        """Check if the game is over and set the winner

        Returns:
            bool: True if the game is over, False otherwise
        """
        # 1. Check horizontal
        for x in range(self.board_size - 4):
            for y in range(self.board_size):
                if self.board[x][y] == self.board[x + 1][y] == self.board[x + 2][y] == self.board[x + 3][y] == self.board[x + 4][y] != self.empty_mark:
                    self.winner = self.board[x][y]
                    return True

        # 2. Check vertical
        for x in range(self.board_size):
            for y in range(self.board_size - 4):
                if self.board[x][y] == self.board[x][y + 1] == self.board[x][y + 2] == self.board[x][y + 3] == self.board[x][y + 4] != self.empty_mark:
                    self.winner = self.board[x][y]
                    return True

        # 3. Check diagonal (top left to bottom right)
        for x in range(self.board_size - 4):
            for y in range(self.board_size - 4):
                if self.board[x][y] == self.board[x + 1][y + 1] == self.board[x + 2][y + 2] == self.board[x + 3][y + 3] == self.board[x + 4][y + 4] != self.empty_mark:
                    self.winner = self.board[x][y]
                    return True

        # 4. Check diagonal (top right to bottom left)
        for x in range(self.board_size - 4):
            for y in range(self.board_size - 4):
                if self.board[x + 4][y] == self.board[x + 3][y + 1] == self.board[x + 2][y + 2] == self.board[x + 1][y + 3] == self.board[x][y + 4] != self.empty_mark:
                    self.winner = self.board[x + 4][y]
                    return True

        # 5. Check for draw
        for x in range(self.board_size):
            for y in range(self.board_size):
                if self.board[x][y] == self.empty_mark:
                    return False

        return True
    
    def legal_moves(self, player) -> List[Tuple[Gomoku, int, int]]:
        """Generate a list of legal moves for the given player

        Args:
            player (str): player marker

        Returns:
            List[Tuple[TicTacToe, int, int]]: a list of TicTacToe objects and their corresponding coordinates
        """
        pass
