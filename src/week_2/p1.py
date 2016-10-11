for month in range(0,12):
    minimumPayment = balance * monthlyPaymentRate
    unpaidBalance = balance - minimumPayment
    interest = (annualInterestRate / 12) * unpaidBalance
    balance = unpaidBalance + interest

print("Remaining balance: {0:.2f}".format(balance))
