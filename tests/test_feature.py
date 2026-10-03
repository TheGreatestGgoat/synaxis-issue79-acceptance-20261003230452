import unittest

from src.feature import greeting


class GreetingTest(unittest.TestCase):
    def test_greeting_names_the_operator(self):
        self.assertEqual(greeting("Synaxis"), "Hello, Synaxis!")


if __name__ == "__main__":
    unittest.main()
