from __future__ import annotations
from typing import List
from copy import deepcopy

class TicTacToe():
    def __init__(self, board: List[List[str]] = None) -> None:
        """Initialize the board

        Args:
            board (List[List[str]], optional): The new board state to copy from, defaults to None.
        """
        self.player_marker = 'X'
        self.opponent_marker = 'O'
        self.empty_mark = '_'
        self.board = [[self.empty_mark] * 3 for _ in range(3)] if board is None else board
        self.winner = None

    def __repr__(self) -> str:
        """Return a string representation of the board

        Returns:
            str: string representation of the board
        """
        ret_str = ''
        for i in range(3):
            ret_str += f'  {i}'
        ret_str += '\n'
        for row in range(3):
            ret_str += f'{row}'
            for col in range(3):
                ret_str += f' {self.board[row][col]} '
            ret_str += '\n'
        return ret_str

    def is_game_over(self) -> bool:
        """Check if the game is over and set the winner

        Returns:
            bool: True if the game is over, False otherwise
        """
        for row in self.board:
            if row[0] == row[1] == row[2] != self.empty_mark:
                self.winner = row[0]
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != self.empty_mark:
                self.winner = self.board[0][col]
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != self.empty_mark:
            self.winner = self.board[0][0]
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != self.empty_mark:
            self.winner = self.board[0][2]
            return True
        
        # If there is no winner, return True if there is no empty space
        counter = 0
        for row in self.board:
            counter += row.count(self.empty_mark)
        if counter == 0:
            return True
        return False

    def legal_moves(self, player) -> List[TicTacToe]:
        """Generate a list of legal moves for the given player

        Args:
            player (str): player marker

        Returns:
            List[Game]: a list of TicTacToe objects
        """
        mark = self.player_marker if player else self.opponent_marker
        possible_moves = []
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == self.empty_mark:
                    new_board = deepcopy(self.board)
                    new_board[row][col] = mark
                    possible_moves.append(TicTacToe(new_board))
        return possible_moves
    
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
    
    def evaluate(self) -> int:
        """Evaluate the board for the given player

        Args:
            player (str): player marker

        Returns:
            int: 1 if the player has won, -1 if the player has lost, 0 otherwise
        """
        self.is_game_over()
        if self.winner == self.player_marker:
            return 1
        elif self.winner == self.opponent_marker:
            return -1
        else:
            return 0
