from ..main.technical_indicators import moving_averages

def run_tests():
    """
    This function executes the tests in the file
    """

    # Technical Indicator Tests
    print('Executing technical indicators tests...')

    # Moving Averages
    print('Testing Simple Moving Average (SMA)...')
    technical_indicators_test_1_sma()

def technical_indicators_test_1_sma():
    # Test variables
    prices = [1]
    n = 1

    # Expected output 
    expected = 1

    # Test output
    test_sma_1 = moving_averages.sma(n, prices)

    if test_sma_1 == expected:
        print('Passed: test_sma_1')
    else:
        print('Failed: Test test_sma_1')

run_tests()