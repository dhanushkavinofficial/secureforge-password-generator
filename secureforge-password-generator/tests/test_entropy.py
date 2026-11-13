import unittest

from secureforge.entropy import estimate_entropy, rate_strength


class TestEntropy(unittest.TestCase):
    def test_entropy_increases_with_length(self):
        self.assertLess(estimate_entropy(20), estimate_entropy(32))

    def test_known_range(self):
        self.assertGreater(estimate_entropy(32), 180)

    def test_invalid(self):
        with self.assertRaises(ValueError):
            estimate_entropy(5)
        with self.assertRaises(TypeError):
            estimate_entropy("x")

    def test_rating(self):
        self.assertEqual(rate_strength(50), "Weak")
        self.assertEqual(rate_strength(100), "Strong")
        self.assertEqual(rate_strength(200), "Very strong")


if __name__ == "__main__":
    unittest.main()
