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

print_fibonacci_seq(10000)