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


def userPrompt():
  """
  """
  pass


class PrimeTest(unittest.TestCase):
  def setUp(self):
    """
    Set up numbers to test for primality.
    """
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
      print "Testing %s" %(number)
      self.assertEqual(isPrime(number), expected)


if __name__ == "__main__":
  if "test" in sys.argv[1:]:
    unittest.main()
  else:
    userPrompt()
