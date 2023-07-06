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
    
    alpha = 2.0 / (n + 1.0)

    # TODO: Figure out how to check for negative prices recursively

    # TODO: Change ema calculation to depend on a different var or be iterative
    # Compute EMA
    if n > 1:
        return ema_helper(alpha, prices)
    else:
        return sma(n, prices)

def ema_helper(alpha, prices):
        # Base Case
        if len(prices) <= 1:
            return sma(len(prices), prices)
        else:
            return ((prices[-1] - prices[-2]) * alpha + ema_helper(alpha, prices[:-1]))