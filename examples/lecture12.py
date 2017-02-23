# Python passes by value, but watch out for Lists!

bank_accounts = ["a", "b", "c", "d"]

# `accounts` is a List type []
def grow_money(accounts, money_to_add):
    for i in range(len(accounts)):
        accounts[i] = accounts[i] + money_to_add


return_grow_money = grow_money(bank_accounts, 100.00)

print("Return of grow money is: ")
print(return_grow_money)

print("The new bank accounts are: ")
print(bank_accounts)

