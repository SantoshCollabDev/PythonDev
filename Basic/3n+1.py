''' 3n + 1 problem

Take the input from the user

If the input is even divide it by 2 and if the input is odd calculate ( 3 * input + 1 )
continue doing the above step till the value becomes 1 

print all the transitions
'''

number = int(input("enter a number"))

while True:
  if number == 1:
    break
  elif number%2 == 0:
    number = number // 2
  elif number%2 == 1:
    number = ( 3 * number) + 1
  print(number)
