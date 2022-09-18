import unittest
import calc


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = calc.Calculator()

    def test_1(self):
        line = '1 + 2'
        self.assertEqual(self.calculator.parse(line), 3)

    def test_2(self):
        line = '(1 + 2) * 5'
        self.assertEqual(self.calculator.parse(line), 15)

    def test_3(self):
        line = '1 + 2 * 5'
        self.assertEqual(self.calculator.parse(line), 11)

    def test_4(self):
        line = '(1+2) / 3'
        self.assertEqual(self.calculator.parse(line), 1)

    def test_5(self):
        line = '81 * 10 / 2'
        self.assertEqual(self.calculator.parse(line), 405)

    def test_6(self):
        line = '144 / (6 * 2)'
        self.assertEqual(self.calculator.parse(line), 12)

    def test_7(self):
        line = '512 / 2 + 5'
        self.assertEqual(self.calculator.parse(line), 261)

    def test_8(self):
        line = '12 * 12 / (10 - 4)'
        self.assertEqual(self.calculator.parse(line), 24)

    def test_9(self):
        line = '8000 + (30 / 10) * 15'
        self.assertEqual(self.calculator.parse(line), 8045)

    def test_10(self):
        line = '15 - (-15)'
        self.assertEqual(self.calculator.parse(line), 30)


if __name__ == '__main__':
    unittest.main()
