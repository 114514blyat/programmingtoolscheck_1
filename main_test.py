import unittest
from main import print_hi_stephen, print_hi_you, print_hi_blyat


class MyTestCase(unittest.TestCase):
    def test_print_hi_stephen(self):
        self.assertEqual(print_hi_stephen(), f"Hi, Stephen")

    def test_print_hi_you(self):
        self.assertEqual(print_hi_you(), f"Hi, Steven")

    def test_print_hi_blyat(self):
        self.assertEqual(print_hi_blyat(), f"Hi, Blyat")
    #def test_print_hi_?(self):
        #


if __name__ == '__main__':
    unittest.main()
