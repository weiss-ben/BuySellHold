import unittest
from ..main.technical_indicators import moving_averages

class TestMovingAverages(unittest.TestCase):

    # SMA Test
    def test_sma(self):
        # Valid
        self.assertEqual(1, moving_averages.sma(1, [1]))

        # In-valid

###### Run Tests #####
unittest.main()