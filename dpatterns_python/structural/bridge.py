"""
bridge pattern in python
"""


class DrawingAPIOne:
    """Implementation-specific abstraction: concrete class one"""

    @staticmethod
    def draw_circle(x_loc, y_loc, radius):
        """
        draw_circle
        :param x_loc:
        :param y_loc:
        :param radius:
        :return:
        """
        print(
            "API 1 drawing a circle at ({}, {} with radius {}!)".format(
                x_loc, y_loc, radius
            )
        )


class DrawingAPITwo:
    """Implementation-specific abstraction: concrete class two"""

    @staticmethod
    def draw_circle(x_loc, y_loc, radius):
        """
        draw_circle
        :param x_loc:
        :param y_loc:
        :param radius:
        :return:
        """
        print(
            "API 2 drawing a circle at ({}, {} with radius {}!)".format(
                x_loc, y_loc, radius
            )
        )


class Circle:
    """Implementation-independent abstraction: for example, there could be a rectangle class!"""

    def __init__(self, x, y, radius, drawing_api):
        """Initialize the necessary attributes"""
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        """Implementation-specific abstraction taken care of by another class: DrawingAPI"""
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    def scale(self, percent):
        """Implementation-independent"""
        self._radius *= percent


def main():
    """
    Build the first Circle object using API One
    Draw a circle
    Build the second Circle object using API Two
    Draw a circle

    :return:
    """

    circle1 = Circle(1, 2, 3, DrawingAPIOne())
    circle1.draw()
    circle2 = Circle(2, 3, 4, DrawingAPITwo())
    circle2.draw()


if __name__ == "__main__":
    main()
