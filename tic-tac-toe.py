class Board:
    value_cache = {}
    def __init__(self, board=None):
        if board is None:
            self.board = [[' ' for col in range(3)] for row in range(3)]
        else:
            self.board = board

    def __str__(self):
        board = ''
        for row in self.board:
            board += "|".join(row) + '\n'
        return board

    @property
    def finished(self):
        return self.won_player() is not None or self.full

    @property
    def full(self):
        for row in self.board:
            for i in row:
                if i == ' ':
                    return False
        return True

    def get_player(self):
        """ gets current player by checking number of turns on self.board """
        turns = 0
        for r in self.board:
            for i in r:
                if i != ' ':
                    turns += 1
        return 'X' if turns%2 == 0 else 'O'

    def get_value(self):
        """ gets value of board: 1 is win for X, -1 is win for O, and 0 is tie """
        winner = self.won_player()
        if winner == 'X': return 1
        if winner == 'O': return -1
        if self.full: return 0

        s = str(self)
        if s in self.value_cache:
            return self.value_cache[s]
        else:
            value = self.get_best_child().get_value()
            self.value_cache[s] = value
            return value

    def get_children(self):
        """ returns all possiblilties for next board """
        children = []
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                if self.board[row][col] == ' ':
                    child = Board([r[:] for r in self.board])
                    child.board[row][col] = self.get_player()
                    children.append(child)
        return children

    def get_best_child(self):
        """ returns child with highest value for current player """
        children = self.get_children()
        if not children:
            return None
        children_values = []
        for child in children:
            children_values.append(child.get_value())
        player = self.get_player()
        key = lambda c: c.get_value()
        return max(children, key=key) if player == 'X' else min(children, key=key)

    def three_same(self, ls):
        """ returns value if all three list items are the same and a valid player or None if they are different """
        a, b, c = ls
        if a == b and b == c:
            if a == 'X' or a == 'O':
                return a
        else:
            return None
    
    def won_player(self):
        """ returns the player who has won. If no one has won, returns None """
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

def play_game(human_player='X'):
    board = Board()

    while not board.finished:
        if board.get_player() == human_player:
            row = input("Enter row: ")
            col = input("Enter col: ")
            board.board[row][col] = human_player
        else:
            board = board.get_best_child()

        print board
            
    print "Game Over! %s won!" % board.won_player()

if __name__ == '__main__':
    board = Board()

    X = 'X'
    O = 'O'
    _ = ' '

    print board.get_value()
    board.board = [[X,_,X],
                   [O,_,O],
                   [X,O,_]]
    assert board.get_value() == 1
    
    board.board = [[X,_,X],
                   [O,_,O],
                   [X,_,_]]
    assert board.get_value() == -1

    board.board = [[X,X,O],
                   [O,O,O],
                   [X,O,X]]
    assert board.get_value() == -1

    board.board = [[X,O,_],
                   [_,X,_],
                   [_,_,_]]

    print "Tests finished"

    play_game()
    play_game('O')
