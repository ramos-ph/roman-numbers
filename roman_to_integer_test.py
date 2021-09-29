from roman_to_integer import roman_to_integer
import unittest

class RomanToIntegerTest(unittest.TestCase):
  def test_mistype(self):
    # Test conversion when type of input is not a string
    self.assertRaises(TypeError, roman_to_integer, 10)
    self.assertRaises(TypeError, roman_to_integer, 11.5)
    self.assertRaises(TypeError, roman_to_integer, True)
    self.assertRaises(TypeError, roman_to_integer, None)
    self.assertRaises(TypeError, roman_to_integer, [1, 2, 3])

  def test_characters(self):
    # Test conversion when one of the letters of the input is not on the roman numerals
    self.assertRaises(ValueError, roman_to_integer, "F")
    self.assertRaises(ValueError, roman_to_integer, "G")
    self.assertRaises(ValueError, roman_to_integer, "H")

  def test_numbers(self):
    # Test conversion when input is a valid roman number
    self.assertEqual(roman_to_integer("I"), 1)
    self.assertEqual(roman_to_integer("III"), 3)
    self.assertEqual(roman_to_integer("V"), 5)
    self.assertEqual(roman_to_integer("X"), 10)
    self.assertEqual(roman_to_integer("XXX"), 30)
    self.assertEqual(roman_to_integer("LX"), 60)
    self.assertEqual(roman_to_integer("C"), 100)
    self.assertEqual(roman_to_integer("D"), 500)
    self.assertEqual(roman_to_integer("DC"), 600)
    self.assertEqual(roman_to_integer("M"), 1000)
    self.assertEqual(roman_to_integer("MMM"), 3000)