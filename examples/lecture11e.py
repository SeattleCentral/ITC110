def move(x=0, dx=10, y=0, dy=10):
    x = x + dx
    y = y + dy
    return x, y

x = 50
y = 50

new_x, new_y = move(x, 50, y, -25)
print("The new coords are: ", new_x, ",", new_y)

print("Call with missing x and y...")
missing_x, missing_y = move(dx=50, dy=50)
print("The new coords are: ", missing_x, ",", missing_y)
