from graphics import *

def handle_key(key, win):
    if key == 'r':
        win.setBackground('pink')
    elif key == 'w':
        win.setBackground('white')
    elif key == 'g':
        win.setBackground('green')    
    elif key == 'b':
        win.setBackground('lightblue')

def handle_click(point, win):
    entry = Entry(point, 10)
    entry.draw(win)

    # Enter inner loop
    while True:
        key = win.getKey()
        if key == 'Return':
            break

    entry.undraw()
    typed = entry.getText()
    Text(point, typed).draw(win)

    # Clear out any mouse clicks that may have occured during text entry
    win.checkMouse()

def main():
    win = GraphWin('Click and Type', 500, 500)

    while True:
        key = win.checkKey()
        if key == 'q':
            break

        if key:
            handle_key(key, win)

        point = win.checkMouse()
        if point:
            handle_click(point, win)

    win.close()

if __name__ == '__main__':
    main()







