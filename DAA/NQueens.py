class NQueens:
    def __init__(self, N, placed):
        self.N = N
        self.placed = placed
        self.board = [[0] * N for _ in range(N)]
        self.board[placed[0]][placed[1]] = 1

    def print_board(self):
        for row in self.board:
            print(" ".join("Q" if cell == 1 else "_" for cell in row))
        print()

    def is_safe(self, pos_x, pos_y):
        for i in range(self.N):
            if self.board[i][pos_y] == 1:
                return False

        for i in range(self.N):
            if self.board[pos_x][i] == 1:
                return False

        i, j = pos_x, pos_y
        while i >= 0 and j >= 0:
            if self.board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        i, j = pos_x, pos_y
        while i < self.N and j >= 0:
            if self.board[i][j] == 1:
                return False
            i += 1
            j -= 1

        i, j = pos_x, pos_y
        while i >= 0 and j < self.N:
            if self.board[i][j] == 1:
                return False
            i -= 1
            j += 1

        i, j = pos_x, pos_y
        while i < self.N and j < self.N:
            if self.board[i][j] == 1:
                return False
            i += 1
            j += 1

        return True

    def solve_n_queens(self, col):
        if col >= self.N:
            return True

        if col == self.placed[1]:
            return self.solve_n_queens(col + 1)

        for i in range(self.N):
            if i == self.placed[0]:
                continue

            if self.is_safe(i, col):
                self.board[i][col] = 1

                if self.solve_n_queens(col + 1):
                    return True

                self.board[i][col] = 0

        return False


def main():
    N = int(input("Enter the Size of the Board (N):"))
    row = int(input("Enter the Row of the Pre-placed Queen:"))
    col = int(input("Enter the Column of the Pre-placed Queen:"))

    n_queens = NQueens(N, (row, col))

    print("\nInitial Board:")
    n_queens.print_board()

    if n_queens.solve_n_queens(0):
        print("Solution:")
        n_queens.print_board()
    else:
        print("No Solution Exists")


if __name__ == "__main__":
    main()
