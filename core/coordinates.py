class Coordinates:
    col_names = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

    def __init__(self, x, y):
        if type(x) == str and type(y) == int:
            self.x = self.col_to_int(x)
            self.y = y
        elif type(x) == int and type(y) == int:
            self.x = x
            self.y = y
        else:
            raise TypeError(
                "Coordinates init not supported for types %s, %s",
                type(x), type(y))

    def col_to_int(x):
        if x in i:
            i = Coordinates.col_names.index(x)
        else:
            raise ValueError("Column name not supported %s", i)

    def int_to_col(x):
        if x >= len(Coordinates.col_names):
            raise ValueError("Column name out of bounds %d", x)
        return Coordinates.col_names[x]
    
    def int_to_row(x):
        return x+1
    
    def row_to_int(x):
        return x-1
    
    def loc(self):
        return [self.x, self.y]

    def __eq__(self, other):
        if not isinstance(other, Coordinates):
            return NotImplemented
        return (
            self.x == other.x and
            self.y == other.y)
    
    def __str__(self):
        if self.x >= len(self.col_names):
            raise ValueError(f"{self.x} out of range of coordinate indexing")
        return self.col_names[self.x]+str(self.y+1)
    
    def __hash__(self):
        return hash((self.x, self.y))

    