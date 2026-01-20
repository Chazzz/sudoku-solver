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

