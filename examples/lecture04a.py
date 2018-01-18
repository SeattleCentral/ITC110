
def main():
    print("This program calculates the future value of a 10-year investment.")

    principle = float(input("Enter the initial principle: "))
    # 1, 3, 7 => int()
    # 2.33, 5.44 => float()
    apr = float(input("Enter the annual percentage rate: "))
    years = int(input("Number of years to invest: "))

    for i in range(years):
        principle = principle * (1 + apr)

    principle_text = "The investment value after {0} years is {1}.".format(
        years, principle)

    print(principle_text)


# import pdb; pdb.set_trace()
if __name__ == '__main__':
    main()
