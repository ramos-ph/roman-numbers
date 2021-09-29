numerals = {
  1: {
    "1": "I",
    "2": "II",
    "3": "III",
    "4": "IV",
    "5": "V",
    "6": "VI",
    "7": "VII",
    "8": "VIII",
    "9": "IX",
  },
  10: {
    "1": "X",
    "2": "XX",
    "3": "XXX",
    "4": "XL",
    "5": "L",
    "6": "LX",
    "7": "LXX",
    "8": "LXXX",
    "9": "XC"
  },
  100: {
    "1": "C",
    "2": "CC",
    "3": "CCC",
    "4": "CD",
    "5": "D",
    "6": "DC",
    "7": "DCC",
    "8": "DCCC",
    "9": "CM",
  },
  1000: {
    "1": "M",
    "2": "MM",
    "3": "MMM"
  }
}

def integer_to_roman(number): 
  if not isinstance(number, int) or isinstance(number, bool):
    raise TypeError("Input type must be an integer.")

  if number < 1:
    raise ValueError("Number must be greater than 0.")

  characters = list(str(number))
  characters.reverse()

  mult = 1
  roman_number = ""

  for char in characters:
    if char != "0":
      roman_number = numerals[mult][char] + roman_number
    mult = mult * 10

  return roman_number
  