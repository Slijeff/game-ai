from game import Game

class TicTacToe(Game):
    def __init__(self):
        self.board = [[' '] * 3 for _ in range(3)]

    def print_board(self):
        print('\n' + '\n'.join([' '.join(row) for row in self.board]))

    def is_game_over(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                self.winner = row[0]
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                self.winner = self.board[0][col]
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            self.winner = self.board[0][0]
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            self.winner = self.board[0][2]
            return True
        return False
    
    def legal_moves(self, player) -> Game:
      pass