class tic_tac_toe:
    def __init__(self):
        self.board = [[0]*4 for i in range(4)]
        self.player = 1

    def get_open_spots(self):
        open_list = []
        for first_row in range(4):
            for each_column in range(4):
                if self.board[first_row][each_column] == 0:
                    open_list.append([first_row,each_column])
        return open_list

    def is_valid_move(self,row,col):
        if [row,col] in self.get_open_spots():
            return True
        else:
            return False

# asking if its valid move before running make_move
    def make_move(self,row,col):
        self.board[row][col] = self.player

        for i in self.board:
            print(i)
            
        if self.player == 1:
            self.player = 2
        else:
            self.player = 1

    def check_for_winner(self):
        each_row1 = []
        each_col1 = []

        each_row2 = []
        each_col2 = []

        i = 0
        while i < len(range(4)):
            j = 0
            while j < len(range(4)):
                if self.board[i][j] == 1 or self.board[j][i] == 1:
                    each_row1.append(self.board[i][j])
                    each_col1.append(self.board[j][i])
                elif self.board[i][j] == 2 or self.board[j][i] == 2:
                    each_row2.append(self.board[i][j])
                    each_col2.append(self.board[j][i])
                j += 1

            if len(each_row1) == 4 or len(each_col1) == 4:
                print("Player 1 win!")
                return 1
            elif len(each_row2) == 8 or len(each_col2) == 8:
                print("Player 2 win!")
                return 2

            each_row1 = []
            each_col1 = []

            each_row2 = []
            each_col2 = []

            i += 1

        if self.board[0][0] == self.board[1][1] == self.board[2][2] == self.board[3][3] == 1:
            print("Player 1 win!")
            return 1
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] == self.board[3][3] == 2:
            print("Player 2 win!")
            return 2
        elif self.board[0][3] == self.board[1][2] == self.board[2][1] == self.board[3][0] == 1:
            print("Player 1 win!")
            return 1
        elif self.board[0][3] == self.board[1][2] == self.board[2][1] == self.board[3][0] == 2:
            print("Player 2 win!")
            return 2


        if len(self.get_open_spots()) == 0:
            print("Draw!")
            return 0
        else:
            return -1

    def playing_game(self):

        while self.check_for_winner() == -1:
            position = input("Enter position player {0}: ".format(self.player))
            real_pos = [int(i) for i in position.split(",")]

            if self.is_valid_move(real_pos[0],real_pos[1]):
                self.make_move(real_pos[0],real_pos[1])
            else:
                print("invalid position, do it again")


def main():
    a = tic_tac_toe()
    a.playing_game()



if __name__ == "__main__":
    main()
