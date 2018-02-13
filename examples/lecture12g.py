
def addInterest(balanceVar, balanceList, rate):
    balanceVar += balanceVar * rate
    for i in range(len(balanceList)):
        balanceList[i] += balanceList[i] * rate


johnsAccount = 500
bankAccounts = [500, 1000, 1500]

addInterest(johnsAccount, bankAccounts, 0.05)

print("John's Account: ", johnsAccount)
print("Bank accounts:")
print(bankAccounts)
