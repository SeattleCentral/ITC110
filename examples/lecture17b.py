from graphics import Rectangle, Point, Circle


class DieView:
    """
    DieView is a widget used to graphically represent a six-sided die
    """

    def __init__(self, win, center, size):
        self.win = win
        self.background = 'white'
        self.foreground = 'black'

        self.pip_size = 0.1 * size
        half_size = size / 2.0
        offset = 0.6 * half_size

        # Create a square die face
        x, y = center.getX(), center.getY()
        point1 = Point(x - half_size, y - half_size)
        point2 = Point(x + half_size, y + half_size)
        rect = Rectangle(point1, point2)
        rect.setFill(self.background)
        rect.draw(win)

        # Create 7 possible pip designs
        self.pip1 = self.__makePip(x - offset, y - offset)
        self.pip2 = self.__makePip(x - offset, y)
        self.pip3 = self.__makePip(x - offset, y + offset)
        self.pip4 = self.__makePip(x, y)
        self.pip5 = self.__makePip(x + offset, y - offset)
        self.pip6 = self.__makePip(x + offset, y)
        self.pip7 = self.__makePip(x + offset, y + offset)

        self.drawValue(1)

    def __makePip(self, x, y):
        pip = Circle(Point(x, y), self.pip_size)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        return pip

    def drawValue(self, value):
        # Reset all pip colors
        pips = [i for i in range(1, 8)]
        self.setPips(pips, self.background)

        # Turn on pips conditionally
        if value == 1:
            self.setPips([4], self.foreground)
        elif value == 2:
            self.setPips([1, 7], self.foreground)
        elif value == 3:
            self.setPips([1, 7, 4], self.foreground)
        elif value == 4:
            self.setPips([1, 3, 5, 7], self.foreground)
        elif value == 5:
            self.setPips([1, 3, 4, 5, 7], self.foreground)
        else:
            self.setPips([1, 2, 3, 5, 6, 7], self.foreground)

    def setPips(self, pips, color):
        for pip_index in pips:
            pip = getattr(self, 'pip{0}'.format(pip_index))
            pip.setFill(color)

