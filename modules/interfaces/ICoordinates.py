from abc import abstractmethod


class ICoordinates:
    @property
    @abstractmethod
    def x(self):
        pass

    @property
    @abstractmethod
    def y(self):
        pass
