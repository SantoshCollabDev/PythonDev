'''
Find the sum of all the multiples of 3 or 5 below 1000
'''

limit_number = 1000

sum = 0
digit = 1

while digit < limit_number:
  if digit%3 == 0 or digit%5 == 0:
    sum += digit
  digit+=1

print(sum)
