# Book version 3

# 1.
print ("Hello, World!")
# Hello, World!
print ("Hello", "World!")
# Hello World!
# ...


# 4.
def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(20):
        x = 3.9 * x * (1 -x)
        print(x)

main()
