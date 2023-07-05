def sma(n, prices):
    """
    Simple moving average (SMA)

    n : number of days to calculate sma over
    prices: data list of security prices
    """
    # Error checking: greater period than prices
    if n > len(prices) or n < 0:
        return -1.0
    
    sum = 0.0
    
    i = 0
    for price in reversed(prices):
        # Error checking: negative prices
        if price < 0.0:
            return -1
        
        # Sum the prices for the specified number of days
        sum += price
        i += 1
            
        # Count back n days
        if i > n:
            break

    # Compute avg
    return sum / n
    
def ema(n, prices):
    """
    Exponential Moving Average (EMA)

    n : number of days to calculate sma over
    prices: data list of security prices
    """
    # DEBUG
    print('length of prices: ', len(prices))

    # Error Checking: greater period than prices or negative period
    if n > len(prices) or n < 0:
        return -1.0
    
    s = 2.0 / (n + 1.0)
    t = prices[-1]
    temp_ema = 0.0

    # TODO: Figure out how to check for negative prices recursively

    # DEBUg
    print('s: ', s)

    # TODO: Change ema calculation to depend on a different var or be iterative
    # Compute EMA
    if n > 1:
        temp_ema += (t * s) + (ema(n, prices[:-1]))
    else:
        # DEBUG
        print('t (else): ', t)
        return sma(n, prices)
    # DEBUG
    print('t: ', t)
    print('Temp EMA: ', temp_ema)
    return temp_ema