""" These tests will test numeric utilities
"""

from loans.numeric import is_prime

def test_is_prime():
  """ Testing prime numbers
  """
  assert is_prime(7) == True
  assert is_prime(6) == False
  assert is_prime(0) == False
