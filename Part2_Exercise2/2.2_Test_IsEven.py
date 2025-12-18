import unittest
from IsEven import is_even


class TestIsEven(unittest.TestCase):
    # TODO:
    # - Write tests for:
    #   * is_even(2) -> True
    #   * is_even(0) -> True
    #   * is_even(7) -> False
    #   * is_even(-4) -> True
    # - Use assertTrue / assertFalse to check the results.
    # - Use clear method names, e.g. test_even_positive_number, etc.
    #
    # write your tests here

    def test_even_positive_number(self):
        self.assertTrue(is_even(2))

    def test_even_zero(self):
        self.assertTrue(is_even(0))

    def test_odd_number(self):
        self.assertFalse(is_even(7))

    def test_even_negative_number(self):
        self.assertTrue(is_even(-4))


if __name__ == "__main__":
    unittest.main()

