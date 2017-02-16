def move(x, dx, y, dy):
    x = x + dx
    y = y + dy
    return x, y

x = 50
y = 50

new_x, new_y = move(x, 50, y, -25)

print("The new coords are: ", new_x, ",", new_y)
