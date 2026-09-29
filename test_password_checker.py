
import unittest

from password_checker import (
    check_length,
    check_uppercase,
    check_lowercase,
    check_number,
    check_special_character,
    check_common_password,
    check_password
)


class TestPasswordChecker(unittest.TestCase):

    def test_length(self):
        self.assertTrue(check_length("Password1"))
        self.assertFalse(check_length("Pass1"))

    def test_uppercase(self):
        self.assertTrue(check_uppercase("Password"))
        self.assertFalse(check_uppercase("password"))

    def test_lowercase(self):
        self.assertTrue(check_lowercase("Password"))
        self.assertFalse(check_lowercase("PASSWORD"))

    def test_number(self):
        self.assertTrue(check_number("Password1"))
        self.assertFalse(check_number("Password"))

    def test_special_character(self):
        self.assertTrue(check_special_character("Password!"))
        self.assertFalse(check_special_character("Password1"))

    def test_common_password(self):
        self.assertFalse(check_common_password("password"))
        self.assertTrue(check_common_password("Xy9!mQ2@"))

    def test_strong_password(self):
        score, rating, checks = check_password("Xy9!mQ2@")

        self.assertEqual(score, 6)
        self.assertEqual(rating, "Strong")
        self.assertTrue(all(checks.values()))

    def test_weak_password(self):
        score, rating, checks = check_password("abc")

        self.assertEqual(score, 2)
        self.assertEqual(rating, "Weak")

    def test_medium_password(self):
        score, rating, checks = check_password("Password")

        self.assertEqual(score, 3)
        self.assertEqual(rating, "Medium")

    def test_none_password(self):
        with self.assertRaises(ValueError):
            check_password(None)


if __name__ == "__main__":
    unittest.main()
