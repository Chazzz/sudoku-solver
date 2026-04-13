from .cell import Cell
from .coordinates import Coordinates

class Cage:
    def __init__(self, coordinates=None, s=0, subcages=[]):
        if not coordinates:
            coordinates = []
        self.coordinates = coordinates
        self.sum = s
        self.subcages = subcages
    
    def __str__(self):
        return f"{[str(c) for c in self.coordinates]} with sum {self.sum}"

    def __contains__(self, item):
        if isinstance(item, Cell):
            return Coordinates(item.x, item.y) in self.coordinates
        if isinstance(item, Coordinates):
            return item in self.coordinates
        if isinstance(item, Cage):
            return all(coord in self.coordinates for coord in item.coordinates)
        if isinstance(item, list):
            return all(coord in self.coordinates for coord in item)