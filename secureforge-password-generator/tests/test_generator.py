import unittest

from secureforge.generator import (
    DIGITS, LOWERCASE, SYMBOLS, UPPERCASE, generate_password,
)


class TestPasswordGenerator(unittest.TestCase):
    def test_password_length(self):
        for n in (20, 32, 128):
            self.assertEqual(len(generate_password(n)), n)

    def test_required_character_categories(self):
        for _ in range(200):
            pw = generate_password(20)
            self.assertTrue(any(c in LOWERCASE for c in pw))
            self.assertTrue(any(c in UPPERCASE for c in pw))
            self.assertTrue(any(c in DIGITS for c in pw))
            self.assertTrue(any(c in SYMBOLS for c in pw))

    def test_invalid_length_value(self):
        for bad in (10, 19, 129):
            with self.assertRaises(ValueError):
                generate_password(bad)

    def test_invalid_length_type(self):
        for bad in ("32", 32.0, None, True):
            with self.assertRaises(TypeError):
                generate_password(bad)

    def test_different_passwords(self):
        self.assertEqual(len({generate_password(32) for _ in range(50)}), 50)


if __name__ == "__main__":
    unittest.main()
