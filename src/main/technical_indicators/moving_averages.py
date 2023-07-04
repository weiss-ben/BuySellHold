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

    s = 2.0 / (n + 1.0)
    t = reversed(prices[0])
    ema = 0.0

    if n > 1:
        ema += (t * s) + (ema(n - 1, prices[:-1]))
    else:
        return sma(n, prices)
    
    return ema