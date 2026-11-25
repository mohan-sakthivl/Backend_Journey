class bank(Exception):
    pass
balance = 5000

try:
    withdraw=int(input("Enter the Amount to withdraw:"))
    
    if withdraw <= balance:
        print("Collect ur cash")
        print("Remaining Balance",balance - withdraw)
    else:
        raise bank("Insufficient balance")
except bank as e:
    print(e)
