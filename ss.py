
import sys

class Sgrid():
    def __init__(self):
        self.grid_size = 9
        self.box_size = 3
        self.grid = [[0, 8, 7, 0, 5, 0, 0, 0, 0],
                     [4, 9, 0, 0, 3, 6, 1, 0, 0],
                     [5, 1, 0, 9, 8, 2, 0, 0, 4],
                     [0, 0, 0, 0, 0, 5, 4, 0, 6],
                     [7, 0, 0, 0, 6, 9, 0, 1, 0],
                     [1, 0, 0, 0, 4, 0, 7, 5, 0],
                     [2, 0, 0, 8, 1, 3, 6, 0, 9],
                     [9, 4, 0, 0, 0, 7, 0, 3, 0],
                     [0, 0, 0, 0, 0, 4, 8, 0, 7]]

    def start(self):
        print("Welcome to Sudoku Solver")
        print("type quit to exit program")
        print("Select an option:\n1: new puzzle\n2: current puzzle")
        choice = self.get_input("> ", [1, 2, 3])
        if choice == 1:
            self.new_puzzle()
        elif choice == 2:
            self.read_puzzle()
            self.solve()

    def new_puzzle(self):
        self.grid.clear()
        print("Select a grid size:\n4: 4x4\n9: 9x9\n16: 16x16")
        choice = self.get_input("> ", [4, 9, 16])
        self.grid_size = choice
        self.box_size = int(choice ** 0.5)

        print(f"Enter values for a new {self.grid_size}x{self.grid_size} board (using 0 for empty cells)")
        for i in range(self.grid_size):
            while True:
                print(f"enter values of row {i+1} ")
                row = self.get_input("> ")
                row_list = [int(char) for char in row]
                if len(row_list) == self.grid_size:
                    self.grid.append(row_list)
                    break
                else:
                    print("\nInvalid entry, try again.\n")
                    pass
        self.write_puzzle("current_puzzle.txt")
        self.show_grid()
        self.solve()

    def read_puzzle(self):
        grid = []
        with open("current_puzzle.txt") as file_object:
            for x in file_object:
                temp_row = []
                temp_row.extend(x)
                grid.append(temp_lst[:-1])
            file_object.close()
        self.grid = grid
        self.grid_size = len(grid)
        self.box_size =  int(self.grid_size ** 0.5)

    def write_puzzle(self, file):
        puzzle = ""
        for r in range(self.grid_size):
            line = ""
            for c in range(self.grid_size):
                line += str(self.grid[r][c]) + " "
            puzzle += line + "\n"

        with open(file, "w") as file_object:
            file_object.write(puzzle)
        file_object.close()

    def get_input(self, prompt, choices=None):
        correct = False

        while not correct:
            choice = input(prompt)
            if choice == "quit":
                sys.exit()
            if choices == None:
                return choice
            try:
                choice = int(choice)
                if choice in choices:
                    return choice
                else:
                    print("\nInvalid entry, try again.\n")
                    continue
            except:
                pass

            try:
                choice = choice.lower()
                if choice in choices:
                    return choice
                else:
                    print("\nInvalid entry, try again.\n")
            except:
                pass


    def show_grid(self):
        print("\n")
        for r in range(self.grid_size):
            line = ""
            for c in range(self.grid_size):
                line += str(self.grid[r][c]) + " "
            print(line)

    def next_empty_cell(self):
        for r in range(self.grid_size):
            for c in range(self.grid_size):
                if self.grid[r][c] == 0:
                    return r, c
        return None, None

    def define_box(self, r, c):
        r_start = (r // self.box_size) * self.box_size
        c_start = (c // self.box_size) * self.box_size
        return r_start, c_start


    def check_val(self, val, r, c,):
        for i in range(self.grid_size):
            if self.grid[r][i] == val:
                return False

        for i in range(self.grid_size):
            if self.grid[i][c] == val:
                return False

        r_start, c_start = self.define_box(r, c)
        for r in range(r_start, r_start + self.box_size):
            for c in range(c_start, c_start + self.box_size):
                if self.grid[r][c] == val:
                    return False
        return True


    def dfs(self):
        r, c = self.next_empty_cell()

        if r == None:
            return True

        for val in range(1,self.grid_size + 1):
            if self.check_val(val, r, c):
                self.grid[r][c] = val
                if self.dfs():
                    return True
            self.grid[r][c] = 0
        return False


    def solve(self):
        if self.dfs():
            self.write_puzzle("complete_puzzle.txt")
            self.show_grid()
            print("Would you like to play again ? (y/n)")
            choice = self.get_input("> ", ["y", "n"])
            if choice == "y":
                self.start()
            else:
                sys.exit()
        else:
            print("Failed to solve")


sgrid = Sgrid()

sgrid.start()
