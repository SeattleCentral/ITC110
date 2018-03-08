from graphics import Point, Rectangle, Text


class Button:

    def __init__(self, win, center, width, height, label='Button'):
        """
        Creates a rectangular button.

        Example usage:
        ==============
        centerPoint = Point(x, y)
        button = Button(win, centerPoint, width, height, 'Click Me!')
        """

        # Get most extreme vertices of button
        half_width = width / 2.0
        half_height = height / 2.0
        x, y = center.getX(), center.getY()
        self.x_min, self.y_min = x - half_width, y - half_height
        self.x_max, self.y_max = x + half_width, y + half_height

        # Create button outline
        point1 = Point(self.x_min, self.y_min)
        point2 = Point(self.x_max, self.y_max)
        self.rect = Rectangle(point1, point2)
        self.rect.setFill('lightgrey')
        self.rect.draw(win)

        # Create button text
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def activate(self):
        """
        Sets this button to "active".
        """
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        """
        Sets this button to "inactive".
        """
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False

    def clicked(self, point):
        """
        Tests to see if the point clicked resides within the button's
        rectangle, and if the button is active.
        """
        if self.active:
            if (self.x_min <= point.getX() and self.y_min <= point.getY() and
                self.x_max >= point.getX() and self.y_max >= point.getY()):
                return True
        return False

    def getLabel(self):
        return self.label.getText()
