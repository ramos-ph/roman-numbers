roman_numerals = {
  "I": 1,
  "V": 5,
  "X": 10,
  "L": 50,
  "C": 100,
  "D": 500,
  "M": 1000
}

def roman_to_integer(string):
  if not isinstance(string, str):
    raise TypeError("Input type must be a string.")

  for letter in string:
    if letter not in roman_numerals.keys():
      raise ValueError(f"Input must consist of the following letters: {', '.join(roman_numerals.keys())}")

  return sum([roman_numerals[letter] for letter in string])
