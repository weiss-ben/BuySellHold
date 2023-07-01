def sma(n, prices):
    """
    Simple moving average (SMA)

    n : number of days to calculate sma over
    prices: data list of security prices
    """
    sum = 0
    
    i = 0
    for price in reversed(prices):
        # Sum the prices for the specified number of days
        sum += price
        i += 1
            
        if i >= n:
            break
            
    return sum / n
    
def ema(n, prices):
    """
    Exponential Moving Average (EMA)

    n : number of days to calculate sma over
    prices: data list of security prices
    """

    s = 2 / (n + 1)
    t = reversed(prices[0])
    ema = 0

    if n > 1:
        ema += (t * s) + (ema(n - 1, prices[:-1]))
    else:
        return sma(n, prices)
    
    return ema