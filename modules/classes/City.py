from modules.interfaces.ICoordinates import ICoordinates


# Description: A city represent the gene of an individual
class City(ICoordinates):
    def __init__(self, position: tuple[int, int]) -> None:
        self.position = position

    @property
    def x(self):
        return self.position[0]

    @property
    def y(self):
        return self.position[1]

    def __eq__(self, other):
        return self.position == other.position

    def __str__(self) -> str:
        return f"City: {self.position}"

    def __hash__(self):
        return hash(self.position)
