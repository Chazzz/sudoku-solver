class Cage:
    def __init__(self, coordinates=None, sum=0):
        if not coordinates:
            coordinates = []
        self.coordinates = coordinates
        self.sum = sum