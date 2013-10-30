class Board:
    def __init__(self):
        self.board = [[' ' for col in range(3)] for row in range(3)]
        self.value = None
        self.move = None

    def __str__(self):
        board = ''
        for row in self.board:
            board += "|".join(row) + '\n'
        return board

    def get_board(self):
        return self.board

    def set_board(self, board):
        self.board = board
        self.value = None

    def is_finished(self):
        return self.check_three_same() is not None or self.is_full()

    def is_full(self):
        for row in self.board:
            for i in row:
                if i == ' ':
                    return False
        return True

    def get_value(self):
        if not self.value:
            self.set_value()
        return self.value

    def set_spot(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.get_player()
            return True
        else:
            return False

    def get_player(self):
        turns = 0
        for r in self.board:
            for i in r:
                if i != ' ':
                    turns += 1
        return 'X' if turns%2 == 0 else 'O'

    def set_value(self):
        winner = self.check_three_same()
        if winner:
            if winner == 'X':
                self.value = 1
            else:
                self.value = -1
        else:
            self.value, self.move = self.create_children()
                
    
    def make_move(self):
        if self.is_finished():
            print self
            return

        if not self.move:
            found = False
            for r in range(len(self.board)):
                for c in range(len(self.board)):
                    if self.set_spot(r, c):
                        found = True
                        break
                if found:
                    break
        else:
            self.set_spot(self.move[0], self.move[1])

        self.move = None
        self.value = None

        print self

    def create_children(self):
        player = self.get_player()
        children_values = []
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                if self.board[row][col] == ' ':
                    child = Board()
                    child.set_board([r[:] for r in self.board])
                    child.set_spot(row, col)
                    children_values.append([child.get_value(), (row, col)])
        if not children_values:
            return [0, None]

        return max(children_values) if player == 'X' else min(children_values)

    def three_same(self, ls):
        a, b, c = ls
        if a == b and b == c:
            if a == ' ':
                return None
            else:
                return a
        else:
            return None
    
    def check_three_same(self):
        size = len(self.board)
        size_range = range(size)

        successful_player = None
        for row in self.board:
            successful_player = successful_player or self.three_same(row)
        for col in size_range:
            successful_player = successful_player or self.three_same([self.board[r][col] for r in size_range])
        successful_player = successful_player or self.three_same([self.board[i][i] for i in size_range])
        successful_player = successful_player or self.three_same([self.board[i][size-1-i] for i in size_range])

        return successful_player

def play_game():


    while not board.is_finished():
        if board.get_player() == 'X':
            row = input("Enter row: ")
            col = input("Enter col: ")
            board.move = (row, col)
            board.make_move()
        else:
            board.get_value()
            board.make_move()

    print "Game Over!"


if __name__ == '__main__':
    board = Board()

    X = 'X'
    O = 'O'
    _ = ' '

    #print board.get_value()
    board.set_board([[X,_,X],
                     [O,_,O],
                     [X,O,_]])
    assert board.get_value() == 1
    
    board.set_board([[X,_,X],
                     [O,_,O],
                     [X,_,_]])
    assert board.get_value() == -1

    board.set_board([[X,X,O],
                     [O,O,O],
                     [X,O,X]])
    assert board.get_value() == -1
    
    
