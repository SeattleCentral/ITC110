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
    pass

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







