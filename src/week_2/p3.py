monthlyInterestRate = annualInterestRate / 12
lowerBound = balance / 12
upperBound = (balance * (1 + monthlyInterestRate) ** 12) / 12

currentBalance = balance
lowestBalance = 0.2

while abs(balance) > lowestBalance:
    balance = currentBalance
    payment = (upperBound - lowerBound) / 2 + lowerBound

    for month in range(12):
        balance -= payment
        balance *= 1 + monthlyInterestRate

    if balance > lowestBalance:
        lowerBound = payment
    else:
        upperBound = payment

print("Lowest Payment: {0:.2f}".format(payment, 2))