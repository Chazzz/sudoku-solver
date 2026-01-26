import json
from .cell import Cell
from .cage import Cage
from .coordinates import Coordinates

class Board:
    def __init__(self):
        cells = []
        for i in range(0,9):
            for j in range(0,9):
                cells.append(Cell(i,j))
        self.cells = cells
        self.cages = []

    def __iter__(self):
        return iter(self.cells)
    
    def __len__(self):
        return len(self.cells)
    
    def __getitem__(self, i):
        return self.cells[i]

    def import_from_command_line(self):
        self.load_json(input("Enter puzzle json:"))
    
    def load_json(self, s):
        data = json.loads(s)
        if "cells" in data:
            for cell in data["cells"]:
                for c in self.cells:
                    if cell["x"] == c.x and cell["y"] == c.y:
                        c.candidates = cell["candidates"]
        if "cages" in data:
            for cage_dict in data["cages"]:
                coordinates = [Coordinates(c["x"], c["y"]) for c in cage_dict["coordinates"]]
                cage = Cage(coordinates, cage_dict["sum"])
                self.cages.append(cage)
    
    def candidates_grid_string(self):
        out = ""
        for row in range(9):
            out += "·-----" * 9 + "·\n"
            for col in range(9):
                out += "| "
                for c in self.cells:
                    if c.x == col and c.y == row:
                        out += "1" if 1 in c.candidates else " "
                        out += "2" if 2 in c.candidates else " "
                        out += "3" if 3 in c.candidates else " "
                out += " "
            out += "|\n"
            for col in range(9):
                out += "| "
                for c in self.cells:
                    if c.x == col and c.y == row:
                        out += "4" if 4 in c.candidates else " "
                        out += "5" if 5 in c.candidates else " "
                        out += "6" if 6 in c.candidates else " "
                out += " "
            out += "|\n"
            for col in range(9):
                out += "| "
                for c in self.cells:
                    if c.x == col and c.y == row:
                        out += "7" if 7 in c.candidates else " "
                        out += "8" if 8 in c.candidates else " "
                        out += "9" if 9 in c.candidates else " "
                out += " "
            out += "|\n"
        out += "·-----" * 9 + "·"
        return out



