import pandas as pd
import tabulate
import random

x = "X"
o = "O"
columns = ['A', 'B', 'C']
data = [['', '', ''], ['', '', ''], ['', '', '']]

class Board:
    def __init__(self, difficulty="Random"):
        self.difficulty = difficulty

        self.board = None
        self.winner = None
        self.move_number = None
        self.valid_locations = None
        self.current_player = None

    def reset_board(self):
        self.board = pd.DataFrame(data, columns=columns)
        self.winner = False
        self.move_number = 0
        self.current_player = random.choice(['p', 'c'])
        self.valid_locations = ["A 0", "A 1", "A 2", "B 0", "B 1", "B 2", "C 0", "C 1", "C 2"]

        if self.current_player == 'p':
            print("Player goes first.")
        else:
            print("Computer goes first.")

    def set_difficulty(self, diff: str) -> None:
        self.difficulty = diff
            
    def next_move(self):
        if self.current_player == 'p':
            self.get_human_players_move()
            self.current_player = 'c'
        else:
            self.move_computer_player()
            self.current_player = 'p'

    def make_move(self, row, col):
        self.valid_locations.pop(self.valid_locations.index(f"{col} {row}"))

        if self.move_number % 2 == 0:
            self.board.at[self.board.index[row], col] = 'X'
        else:
            self.board.at[self.board.index[row], col] = 'O'

        self.move_number += 1

        self.check_win_condition()

    def check_win_condition(self):
        for i in range(0, 3):
            # check all rows
            if self.board.iloc[i].sum() == "XXX":
                self.winner = "X"
                return
            elif self.board.iloc[i].sum() == "OOO":
                self.winner = "O"
                return

        for c in ['A', 'B', 'C']:
            # check all columns
            if self.board[c].sum() == "XXX":
                self.winner = "X"
                return
            if self.board[c].sum() == "OOO":
                self.winner = "O"
                return

        # check diagonals
        left_diag = self.board.loc[0, 'A'] + self.board.loc[1, 'B'] + self.board.loc[2, 'C']
        if left_diag == "XXX":
            self.winner = "X"
            return
        elif left_diag == "OOO":
            self.winner = "O"
            return

        right_diag = self.board.loc[0, 'C'] + self.board.loc[1, 'B'] + self.board.loc[2, 'A']
        if right_diag == 'XXX':
            self.winner = "X"
            return
        elif right_diag == "OOO":
            self.winner = "O"
            return

        if self.move_number == 9:
            self.winner = "DRAW"
            return

    def print(self):
        print(self.board.to_markdown(tablefmt='grid'))

    def move_computer_player(self):
        if self.difficulty == 'Random':
            move = random.choice(self.valid_locations)
            row = int(move.split()[1])
            col = move.split()[0]
            self.make_move(row=row, col=col)
        else:
            pass

    def get_human_players_move(self):
        marks = 1
        try:
            move = input("What is your move? (ftm=column row):")
            move = move.strip()
            if len(move) == 2:
                col = move[0].upper()
                row = int(move[1])
            else:
                col = move.split()[0].upper()
                row = int(move.split()[1])

            self.make_move(row=row, col=col)

        except:
            print(f"invalid move format, or move already taken. marks:{marks}")
            marks += 1
            if marks == 3:
                exit()
            self.get_human_players_move()
