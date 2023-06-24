'''
Simple moving average (SMA)

num_days : number of days to calculate sma over
'''
def sma(num_days, prices):
    sum = 0
    
    i = 0
    for price in reversed(prices):
        # Sum the prices for the specified number of days
        sum += price
        i += 1
            
        if i >= num_days:
            break
            
    return sum / num_days
    
'''
Exponential Moving Average (EMA)

num_days : number of days to calculate sma over
'''
def ema(num_days, prices):
    sum = 0
    
    i = 0
    
    for price in reversed(prices):
        # Calculate the ema
        
    return sum / num_days