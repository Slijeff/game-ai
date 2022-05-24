from __future__ import annotations
from typing import List, Tuple
from copy import deepcopy
from multiprocessing import Process, Queue


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

        answers = Queue()
        processes = [
            Process(target=self._check_horizontal, args=(answers,)),
            Process(target=self._check_vertical, args=(answers,)),
            Process(target=self._check_diagonal_tlbr, args=(answers,)),
            Process(target=self._check_diagonal_trbl, args=(answers,))
        ]
        for p in processes:
            p.start()
        for p in processes:
            p.join()
        for _ in range(4):
            terminated, winner = answers.get()
            if terminated:
                self.winner = winner
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
            List[Tuple[Gomoku, int, int]]: a list of TicTacToe objects and their corresponding coordinates
        """
        mark = self.player_marker if player else self.opponent_marker
        possible_moves = []
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row][col] == self.empty_mark:
                    new_board = deepcopy(self.board)
                    new_board[row][col] = mark
                    possible_moves.append((Gomoku(new_board), row, col))
        return possible_moves

    def evaluate(self) -> int:
        """Evaluate the board for the given player

        Args:
            player (str): player marker

        Returns:
            int: Positive higher score indicates better move for current player
        """
        ...

    # 1. Check horizontal
    def _check_horizontal(self, q: Queue) -> bool:
        for x in range(self.board_size - 4):
            for y in range(self.board_size):
                if self.board[x][y] == self.board[x + 1][y] == self.board[x + 2][y] == self.board[x + 3][y] == self.board[x + 4][y] != self.empty_mark:
                    q.put([True, self.board[x][y]])
                    return
        q.put([False, None])

    # 2. Check vertical
    def _check_vertical(self, q: Queue) -> bool:
        for x in range(self.board_size):
            for y in range(self.board_size - 4):
                if self.board[x][y] == self.board[x][y + 1] == self.board[x][y + 2] == self.board[x][y + 3] == self.board[x][y + 4] != self.empty_mark:
                    q.put([True, self.board[x][y]])
                    return
        q.put([False, None])

    # 3. Check diagonal (top left to bottom right)
    def _check_diagonal_tlbr(self, q: Queue) -> bool:
        for x in range(self.board_size - 4):
            for y in range(self.board_size - 4):
                if self.board[x][y] == self.board[x + 1][y + 1] == self.board[x + 2][y + 2] == self.board[x + 3][y + 3] == self.board[x + 4][y + 4] != self.empty_mark:
                    q.put([True, self.board[x][y]])
                    return
        q.put([False, None])

    # 4. Check diagonal (top right to bottom left)
    def _check_diagonal_trbl(self, q: Queue) -> bool:
        for x in range(self.board_size - 4):
            for y in range(self.board_size - 4):
                if self.board[x + 4][y] == self.board[x + 3][y + 1] == self.board[x + 2][y + 2] == self.board[x + 1][y + 3] == self.board[x][y + 4] != self.empty_mark:
                    q.put([True, self.board[x][y]])
                    return
        q.put([False, None])
