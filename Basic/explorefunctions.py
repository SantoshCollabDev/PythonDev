import snoop

def is_even(number: int):
  '''
  Args:
    number: number to be tested for even
  
  Returns:
    True if even otherwise False

  Usage:
    is_even(6)
    True
  '''
  if number <= 0:
    return False
  
  result = (number % 2 == 0)
  return result

# for index in range(1,11):
#   if is_even(index):
#     print(index,end=" ")


@snoop
def is_prime(number: int):
  ''' Dtermines if a given number is prime or non-prime 
  Args:
    number: value to be tested for prime

  Returns:
    True if prime otherwise False
  '''
  if number<= 0:
    return False
  for index in range(2,number):
    if number%index == 0:
      return False   
  return True

for value in range(10,12):
  if is_prime(value):
    print(value)