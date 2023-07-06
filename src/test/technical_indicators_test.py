import unittest
from ..main.technical_indicators import moving_averages

class TestMovingAverages(unittest.TestCase):

    # SMA Test
    def test_sma(self):
        #### Valid ###
        # Single value, single day
        self.assertEqual(1.0, moving_averages.sma(1, [1.0]))
        # Multiple values, multiple days
        self.assertTrue((abs(12.222 - moving_averages.sma(9.0, [2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0]))) <= 0.01)

        #### In-valid ####
        # Invalid: Single Value, Multiple days
        self.assertEqual(-1.0, moving_averages.sma(10, [33.234]))
        # Invalid: negative n
        self.assertEqual(-1.0, moving_averages.sma(-3.0, [2.3, 3.4, 1.234, 4.234, 4.623]))
        # Invalid: negative prices
        self.assertEqual(-1.0, moving_averages.sma(5, [4.23, 89.34, -17.098, 12.2, 4.234]))
        # Invalid: Empty price list
        self.assertEqual(-1.0, moving_averages.sma(20, []))

    # EMA Test
    def test_ema(self):
        #### Valid ####
        # Single value, Single day period
        self.assertEqual(1.0, moving_averages.ema(1.0, [1.0]))
        # Multiple values, Multiple day period
        #self.assertTrue((abs(8.324 - moving_averages.ema(9.0, [2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0]))) <= 0.01)
        self.assertTrue((abs(3.333 - moving_averages.ema(2.0, [2.0, 4.0]))) <= 0.01)

        #### Invalid ####
        # Invalid: Single value, multiple day period
        # Invalid: Negative n
        # Invalid: Negative prices
        # Invalid: Empty price list
###### Run Tests #####
unittest.main()