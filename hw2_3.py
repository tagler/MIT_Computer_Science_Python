balance = 320000
annualInterestRate = 0.2

monthyInterestRate = annualInterestRate/12

low = balance / 12
high = (balance * ( 1 + monthyInterestRate )**12 ) / 12.0
guess = round( (high+low)/2, 2)

while True:   
    
    temp_balance = balance 
    
    for x in range(1,13):
        unpaidBalance = temp_balance  - guess
        temp_balance  = unpaidBalance + (annualInterestRate/12) * unpaidBalance
    
    if temp_balance < - 0.1:
        low = low
        high = guess
        guess = (low+high)/2
    elif temp_balance > 0.1:
        high = high
        low = guess
        guess = (low+high)/2
    else:
        break
        
print('Lowest payment: ' + str(round(guess,2)))