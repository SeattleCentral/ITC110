
def addInterest(johnsAccount, bankAccounts, rate):
    johnsAccount = johnsAccount + johnsAccount * rate
    for i in range(len(bankAccounts)):
        bankAccounts[i] = bankAccounts[i] + bankAccounts[i] * rate
    print("John's Account: ", johnsAccount)
    print("Bank accounts:", bankAccounts)
    print("Exiting function")


johnsAccount = 500
bankAccounts = [500, 1000, 1500]

addInterest(johnsAccount, bankAccounts, 0.05)

print("John's Account: ", johnsAccount)
print("Bank accounts:", bankAccounts)
