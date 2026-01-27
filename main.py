from core.board import Board
from core.solver import Solver

def main():
    b = Board()
    b.import_from_command_line()
    s = Solver()
    s.solve(b, debug=True)

if __name__ == "__main__":
    main()