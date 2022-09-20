from player import HumanPlayer, ComputerPlayer

class Tic_Tac_Toe():
    def __init__(self):
        self.spots = [" " for spot in range(9)]
        self.winner = False

    def print_board(self):
        # x|x|x
        for row in [self.spots[i * 3:(i + 1) * 3] for i in range(3)]:
            print('|'.join(row))

    @staticmethod
    def print_board_nums():
        # which numbers corresponds to which spot
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print("|".join(row))

    def available_moves(self):
        moves = []
        for (i, spot) in enumerate(self.spots):
            if spot == " ":
                moves.append(i)
        return moves

    def make_move(self, letter, square):
        if self.spots[square] == " ":
            self.spots[square] = letter
            return True
        else:
            return False

    def empty_spots(self):
        return " " in self.spots

    def num_empty_spots(self):
        return len(self.available_moves())

    # How do we know if someone wins?
    def is_winner(self, letter, square):

        #diagonal win
        if all(spot == letter for spot in self.spots[0:8:4]) or all(spot == letter for spot in self.spots[2:6:2]):
            return True

        #row win
        for row in [self.spots[i * 3:(i + 1) * 3] for i in range(3)]:
            if all(spot == letter for spot in row):
                return True

        #column win
        for column in [self.spots[]]


def play(x_player, o_player, game, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X'

    while game.empty_spots():
        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(letter=letter, square=square):
            if print_game:
                print(letter + f" makes a move to square {square}")
                game.print_board()
                game.print_board_nums()
                print(' ')

            if game.is_winner(letter):
                print("we have a winner")

            letter = "O" if letter == "X" else 'X'


game = Tic_Tac_Toe()


x = HumanPlayer(letter="X")
c = HumanPlayer(letter="O")

play(x_player=x, o_player=c, game=game, print_game=True)
