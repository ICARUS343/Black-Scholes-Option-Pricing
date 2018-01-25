import unittest

import black_scholes


class TestBlackScholes(unittest.TestCase):

    def test_call_option(self):
        result = black_scholes.option_value(62.0, 60.0, 40.0 / 365, 0.32, 0.04, True)
        self.assertAlmostEquals(result, 3.84, 1, None, None) # first val, second val, decimal places, msg, delta

    def test_put_option(self):
        result = black_scholes.option_value(62, 60, 40.0 / 365, 0.32, 0.04, False)
        self.assertAlmostEquals(result, 1.50, 1, None, None)

if __name__ == '__main__':
    unittest.main()