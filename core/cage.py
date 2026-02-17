class Cage:
    def __init__(self, coordinates=None, s=0, subcages=[]):
        if not coordinates:
            coordinates = []
        self.coordinates = coordinates
        self.sum = s
        self.subcages = subcages
    
    def __str__(self):
        return f"{[str(c) for c in self.coordinates]} with sum {self.sum}"
