balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

totalPaid = 0

for x in range(1,13):
    
    minPayment = balance * monthlyPaymentRate
    unpaidBalance = balance - minPayment
    balance = unpaidBalance + (annualInterestRate/12) * unpaidBalance
    
    totalPaid = totalPaid + minPayment
    
    print('Month: ' + str(x))
    print('Minimum monthly payment: ' + str(round(minPayment,2)))
    print('Remaining balance: ' + str(round(balance,2)))

print('Total paid: ' + str(round(totalPaid,2)))
print('Remaining balance: ' + str(round(balance,2)))
