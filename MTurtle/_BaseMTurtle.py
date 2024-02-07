from math import cos, radians, sin
from typing import NamedTuple


class MTurtlePoint(NamedTuple):
    x_coordinate: float
    y_coordinate: float


class Line(NamedTuple):
    point1: MTurtlePoint
    point2: MTurtlePoint
    
    @staticmethod
    def calculate_endpoint(
            _point1: MTurtlePoint,
            length: float,
            angle_of_rotation: float
    ) -> MTurtlePoint:
        return MTurtlePoint(
                _point1.x_coordinate + length * cos(radians(angle_of_rotation)),
                _point1.y_coordinate - length * sin(radians(angle_of_rotation)),
        )


class BaseMTurtle:
    __slots__ = ("position", "rotation")
    position: MTurtlePoint
    rotation: float
    
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self):
        super().__init__()
        self.position: MTurtlePoint = MTurtlePoint(0, 0)
        self.rotation: float = 0
    
    def draw_forward(self, _length: float) -> tuple[Line, str]:
        _point1 = MTurtlePoint(self.position.x_coordinate, self.position.y_coordinate)
        _point2 = Line.calculate_endpoint(_point1, _length, self.rotation)
        self.position = _point2
        return Line(_point1, _point2), ""
    
    def draw_backward(self, _length: float) -> tuple[Line, str]:
        _point1 = MTurtlePoint(self.position.x_coordinate, self.position.y_coordinate)
        _point2 = Line.calculate_endpoint(_point1, -_length, self.rotation)
        self.position = _point2
        return Line(_point1, _point2), ""
    
    def move_forward(self, _length: float) -> None:
        self.position = Line.calculate_endpoint(self.position, _length, self.rotation)
    
    def move_backward(self, _length: float) -> None:
        self.position = Line.calculate_endpoint(self.position, -_length, self.rotation)
    
    def turn_left(self, _angle: float) -> None:
        self.rotation -= _angle
    
    def turn_right(self, _angle: float) -> None:
        self.rotation += _angle


def main():
    pass


if __name__ == '__main__':
    main()
