def print_fibonacci_seq(end: int) -> None:

  if end <= 1:
    return None
  
  first = 1
  second = 2
  print(first, second, end=" ")

  while True:
    third = first + second
    if third > end:
      return None
    print(third,end=" ")
    first = second
    second = third

# print_fibonacci_seq(10000)


def get_fibonacci_sequence(end: int):

  if end <= 2:
    return None
  
  first = 1
  second = 2

  fibonacci_sequence = []
  fibonacci_sequence.append(first)
  fibonacci_sequence.append(second)

  while True:
    third = first + second
    if third > end:
      return fibonacci_sequence
    fibonacci_sequence.append(third)
    first = second
    second = third

# sequence = get_fibonacci_sequence(10000)
# print(sequence)

def is_even(number) -> bool:
  if number <= 0:
    return False
  return number % 2 == 0

max = 4000000
sequence = get_fibonacci_sequence(max)
print("fibinacci under 4 million are")
print(sequence)
even_sequence = []
for item in sequence:
  if is_even(item):
    even_sequence.append(item)
print("even numbers in the sequence are as follows")
print(even_sequence)
sum_of_even_fibonacci = sum(even_sequence)
print(sum_of_even_fibonacci)
