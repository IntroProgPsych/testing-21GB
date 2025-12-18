import unittest
from divide import safe_divide


class TestSafeDivide(unittest.TestCase):
    # TODO:
    # - Write tests for:
    #   * safe_divide(10, 2) -> 5.0
    #   * safe_divide(0.5, 0.1) (use assertAlmostEqual)
    #   * safe_divide(5, 0) raises ValueError
    # - Use assertRaises to test the exception.
    # - Use clear method names, e.g. test_division_integers, etc.
    #
    # write your tests here

    def test_division_integers(self):
        self.assertEqual(safe_divide(10, 2), 5.0)

    def test_division_floats(self):
        self.assertAlmostEqual(safe_divide(0.5, 0.1), 5.0)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            safe_divide(5, 0)


if __name__ == "__main__":
    unittest.main()
