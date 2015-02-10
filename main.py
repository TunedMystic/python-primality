#!/usr/bin/env python

import sys
import math
import unittest

"""
--- Assignment ---
Write a program that prompts the user to enter an integer.
If the input value is not an integer greater than one, display
a helpful error message. Otherwise, output 'prime' if the integer
is prime (divisible by 1 and itself), or 'composite' if the
integer is not prime.

Github Repository: https://github.com/TunedMystic/python-primality

To run program:
  > python main.py
  
To run tests:
  > python main.py test
"""


def isPrime(n):
  """
  Test if a number 'n' is prime.
  """
  # The only even number that is prime.
  if n == 2:
    return True
  # 1, 0 and negative numbers are not prime.
  # Even numbers (other than 2) are not prime.
  if n < 2 or n % 2 == 0:
    return False
  # Iterate up to the square root of n.
  # Test only odd numbers greater than 2.
  for i in range(3, int(math.sqrt(n) + 1), 2):
    if n % i == 0:
      return False
  return True


def clean_input(msg):
  """
  Prompts the user for an integer.
  Returns the integer if it is more than 1.
  Returns an error message otherwise.
  """
  try:
    # Attempt to convert the input to an int.
    num = int(raw_input(msg))
    if num <= 1:
      return "%d is not greater than 1. Try again." %(num)
    else:
      return num
  except ValueError:
    # Catch errors during type conversion.
    return "Hmm, that's not an integer. Try again."


def userPrompt():
  """
  Prompt user to enter an integer.
  If integer is less than or equal to 1, print error message.
  If integer is more than 1, test primality and output results.
  """
  while True:
    val = clean_input("\nPlease enter an integer greater than 1.\n> ")
    # If an integer is returned, it is considered 'cleaned'.
    # If a string is returned, it is considered an error message.
    if isinstance(val, int):
      if isPrime(val):
        print "prime"
      else:
        print "composite"
      return
    else:
      print val


class PrimeTest(unittest.TestCase):
  def setUp(self):
    """
    Set up numbers to test for primality.
    """
    self.isPrime = isPrime
    self.values = [
      (-1,  False),
      (0,   False),
      (1,   False),
      (2,    True),
      (7,    True),
      (9,   False),
      (11,   True),
      (40,  False),
      (221, False),
      (2549, True),
    ]
  
  def test_isPrime(self):
    """
    Primality Test.
    """
    for number, expected in self.values:
      print "\nTesting   : %s" %(number)
      print "Expecting : %s"   %(expected)
      result = self.isPrime(number)
      self.assertEqual(result, expected)
      print "Got       : %s" %(result)


if __name__ == "__main__":
  if "test" in sys.argv[1:]:
    sys.argv.pop()
    unittest.main()
  else:
    userPrompt()
