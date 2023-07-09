def sma(n, prices):
    """
    Simple moving average (SMA)

    n : number of days to calculate sma over
    prices: data list of security prices
    """
    # Error checking: greater period than prices
    if n > len(prices) or n < 0:
        return -1.0
    
    # Copy only relevant # of prices from price list
    #price_window = prices[(n - 1):]
    price_window = prices[-n:]

    sum = 0.0
    result = []

    i = 0
    for price in price_window:
        # Error checking: negative prices
        if price < 0.0:
            return -1
        
        # Sum the prices for the specified number of days
        sum += price
        i += 1

        # Compute average and place in list
        avg = sum / i
        result.append(avg)

    return result
    
def ema(n, prices):
    """
    Exponential Moving Average (EMA)

    n: number of days to calculate sma over
    prices: data list of security prices
    """

    # Error Checking: greater period than prices or negative period
    if n > len(prices) or n < 0:
        return -1.0
    
    # Copy only requested window of prices
    price_window = prices[(n - 1):]

    alpha = 2.0 / (n + 1.0)

    # Compute EMA
    if n > 1:
        print(ema_helper(alpha, prices))
        return ema_helper(alpha, prices)
    else:
        return sma(n, prices)

def ema_helper(alpha, prices):
        '''
        Helper for EMA calculation, handles recursive calculation

        alpha: smoothing/weighting factor
        prices: price list
        '''
        # Base Case
        if len(prices) <= 1:
            return sma(len(prices), prices)
        else:
            return ((prices[-1] - prices[-2]) * alpha + ema_helper(alpha, prices[:-1]))