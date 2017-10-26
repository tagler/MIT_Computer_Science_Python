balance = 3329
annualInterestRate = 0.2

guess = int(round(balance / 12,-1))
temp_balance = balance 

while temp_balance > 0:   
    
    for x in range(1,13):
        unpaidBalance = temp_balance  - guess
        temp_balance  = unpaidBalance + (annualInterestRate/12) * unpaidBalance
    
    if temp_balance  < 0:
        break
    else:
        temp_balance = balance     
        guess = guess + 10 

print('Lowest payment: ' + str(guess))