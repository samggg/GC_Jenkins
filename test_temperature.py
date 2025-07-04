import unittest
import temperature

class TestTemperatureConversion(unittest.TestCase):
    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(temperature.fahrenheit_to_celsius(32), 0)

    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(temperature.celsius_to_fahrenheit(100), 212)

if __name__ == '__main__':
    unittest.main()
