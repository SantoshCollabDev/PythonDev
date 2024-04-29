def is_divisible_by_3_or_5(number):
  return (number % 3 == 0) or (number % 5 == 0)

def solution():
  return sum(filter(is_divisible_by_3_or_5,range(1,1000)))
 