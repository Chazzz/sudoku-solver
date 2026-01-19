import json
from .cell import Cell

class Board:
    def __init__(self):
        cells = []
        for i in range(0,9):
            for j in range(0,9):
                cells.append(Cell(i,j))
        self.cells = cells
        self._index = 0

    def __iter__(self):
        return iter(self.cells)
    
    def __len__(self):
        return len(self.cells)

    def import_from_command_line(self):
        self.load_json(input("Enter puzzle json:"))
    
    def load_json(self, s):
        data = json.loads(s)
        for cell in data:
            for c in self.cells:
                if cell["x"] == c.x and cell["y"] == c.y:
                    c.candidates = cell["candidates"]

