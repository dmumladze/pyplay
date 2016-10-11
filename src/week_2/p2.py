minimumPayment = 0
success = False

currentBalance = balance

monthlyInterestRate = annualInterestRate / 12

while not success:
    currentBalance = balance
    minimumPayment = minimumPayment + 10
    for month in range(0, 12):        
        unpaidBalance = currentBalance - minimumPayment
        interest = (annualInterestRate / 12) * unpaidBalance
        currentBalance = unpaidBalance + interest
        #print("Remaining balance: " + str(currentBalance)) 

        if currentBalance <= 0:
            success = True
            break                

print("Lowest Payment: {0:.2f}".format(minimumPayment))