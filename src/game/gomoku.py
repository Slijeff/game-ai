from __future__ import annotations
from typing import List, Tuple
from copy import deepcopy
from multiprocessing import Process, Queue, Pool


class Gomoku:
    def __init__(self, board: List[List[str]] = None) -> None:
        """Initialize the board

        Args:
            board (List[List[str]], optional): The new board state to copy from, defaults to None.
        """
        self.board_size = 15
        self.player_marker = 'x'
        self.opponent_marker = 'o'
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
        # for p in processes:
        #     p.join()
        while answers.qsize() != 4:
            pass
        while not answers.empty():
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
                if self.board[row][col] == self.empty_mark and self._has_neighbor([row, col]):
                    new_board = deepcopy(self.board)
                    new_board[row][col] = mark
                    possible_moves.append((Gomoku(new_board), row, col))
        return possible_moves

    def evaluate(self) -> int:
        """Evaluate the board for the given player

        Notes:
            The evaluation function credits to https://github.com/HuyTtdd/gomoku-minimax

        Args:
            player (str): player marker

        Returns:
            int: Positive higher score indicates better move for current player
        """

        total_score = 0
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.board[i][j] != self.empty_mark or self._has_neighbor([i, j]):
                    row = "".join(self._get_row((i, j)))
                    column = "".join(self._get_column((i, j)))
                    lslash = "".join(self._get_lslash((i, j)))
                    rslash = "".join(self._get_rslash((i, j)))
                    
                    total_score += self._calc_score(row)
                    total_score += self._calc_score(column)
                    total_score += self._calc_score(lslash)
                    total_score += self._calc_score(rslash)

        return total_score

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

    def _get_row(self, p):
        return self.board[p[0]][max(p[1]-4, 0): min(p[1]+5, self.board_size)]


    def _get_column(self, p):
        return [self.board[i][p[1]] for i in range(max(p[0]-4, 0), min(p[0]+5, self.board_size))]


    def _get_lslash(self, p):
        lslash_1 = [self.board[p[0]+i][p[1]+i]
                    for i in range(min(5, self.board_size - max(p[0], p[1])))]
        lslash = [self.board[p[0]-i][p[1]-i]
                for i in range(1, min(5, p[0]+1, p[1]+1))][::-1]

        lslash.extend(lslash_1)

        return lslash


    def _get_rslash(self, p):
        rslash_1 = [self.board[p[0]-i][p[1]+i]
                    for i in range(min(p[0] - max(p[0]-5, -1), min(p[1]+5, self.board_size) - p[1]))]

        rslash = [self.board[p[0]+i][p[1]-i]
                for i in range(1, min(min(p[0]+5, self.board_size) - p[0], p[1] - max(p[1]-5, -1)))][::-1]

        rslash.extend(rslash_1)

        return rslash

    def _has_neighbor(self, p):
        pos = [(-1, -1), (-1, 0), (-1, 1), (0, 1),
            (1, 1), (1, 0), (1, -1), (0, -1)]

        for i in pos:
            try:
                if self.board[p[0]+i[0]][p[1]+i[1]] != self.empty_mark:
                    return True
            except IndexError:
                continue
        return False
    
    def _calc_score(self, list_):
        scores = {0: 99999, 1: 900, 2: 90, 3: 90, 4: 90, 5: 90,
                6: 90, 7: 50, 8: 5, 9: 5, 10: 2, 11: 2, 12: 2, 13: 2}
        pattern_x = ["xxxxx", "_xxxx_", "xxxx_", "_xxxx", "xxx_x", "xx_xx",
                    "x_xxx", "_xxx_", "xxx_", "_xxx", "_x_x_", "_xx_", "_xx", "xx_"]
        pattern_o = ["ooooo", "_oooo_", "oooo_", "_oooo", "ooo_o", "oo_oo",
                    "o_ooo", "_ooo_", "ooo_", "_ooo", "_o_o_", "_oo_", "_oo", "oo_"]

        score = 0

        for index, pattern in enumerate(pattern_x):
            z = list_.find(pattern)
            if z != -1:
                score += scores[index]
                break

        for index, pattern in enumerate(pattern_o):
            z = list_.find(pattern)
            if z != -1:
                score -= scores[index]
                break

        return score