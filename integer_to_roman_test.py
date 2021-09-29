from integer_to_roman import integer_to_roman
import unittest

class IntegerToRomanTest(unittest.TestCase):
  def test_zero(self):
    # Test conversion when input is zero.
    self.assertRaises(ValueError, integer_to_roman, 0)

  def test_negative(self):
    # Test conversion when input is negative.
    self.assertRaises(ValueError, integer_to_roman, -1)
    self.assertRaises(ValueError, integer_to_roman, -10)
    self.assertRaises(ValueError, integer_to_roman, -50)

  def test_mistype(self):
    # Test conversion when type of input is not an integer.
    self.assertRaises(TypeError, integer_to_roman, "10")
    self.assertRaises(TypeError, integer_to_roman, 11.5)
    self.assertRaises(TypeError, integer_to_roman, True)
    self.assertRaises(TypeError, integer_to_roman, None)

  def test_success(self):
    # Test conversion when input is a valid number.
    self.assertEqual(integer_to_roman(1), "I")
    self.assertEqual(integer_to_roman(3), "III")
    self.assertEqual(integer_to_roman(5), "V")
    self.assertEqual(integer_to_roman(10), "X")
    self.assertEqual(integer_to_roman(15), "XV")
    self.assertEqual(integer_to_roman(30), "XXX")
    self.assertEqual(integer_to_roman(60), "LX")
    self.assertEqual(integer_to_roman(100), "C")
    self.assertEqual(integer_to_roman(500), "D")
    self.assertEqual(integer_to_roman(600), "DC")
    self.assertEqual(integer_to_roman(1000), "M")
    self.assertEqual(integer_to_roman(1010), "MX")
    self.assertEqual(integer_to_roman(3000), "MMM")