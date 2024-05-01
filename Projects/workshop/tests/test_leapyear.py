"""This tests the leap year
"""
from workshop.leapyear import is_leap_year, leap_years

def test_is_leap_year():
  """This
  """
  assert is_leap_year(2000) is True
  assert is_leap_year(1996) is True
  assert is_leap_year(2100) is False
  assert is_leap_year(1997) is False


def test_leap_years():
  """ This
  """
  result = leap_years(1996,2005)
  assert len(result) == 3 # checking against 3 since we are expected 3 years
  assert result == [1996,2000,2004]



