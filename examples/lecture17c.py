from graphics import GraphWin, Point

from lecture16h import MultiSidedDie
from lecture17a import Button
from lecture17b import DieView


def main():
    win = GraphWin('Dice Roller')
    win.setCoords(0, 0, 10, 10)
    win.setBackground('green2')

    die1 = MultiSidedDie(6)
    die2 = MultiSidedDie(6)
    dieView1 = DieView(win, Point(3, 7), 2)
    dieView2 = DieView(win, Point(7, 7), 2)

    rollButton = Button(win, Point(5, 4.5), 6, 1, 'Roll Dice')
    rollButton.activate()

    quitButton = Button(win, Point(5, 1), 2, 1, 'Quit')

    point = win.getMouse()
    while not quitButton.clicked(point):
        if rollButton.clicked(point):
            die1.roll()
            dieView1.drawValue(die1.getValue())
            die2.roll()
            dieView2.drawValue(die2.getValue())
            quitButton.activate()
        point = win.getMouse()

    win.close()


if __name__ == '__main__':
    main()
