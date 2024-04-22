'''
Approach: Find individual digits and add them till result is <10 or result is a single digit number 

Digital Root of 1729 ==>

1 + 7 + 2 + 9 = 19
since 19 is a 2 digit number repeat the digit sum process

1 + 9 = 10
since 10 is a 2 digit number repeat the digit sum process

1+ 0 = 1

Since result is a single digit number i.e. < 10 STOP the process
'''

number = int(input("enter a number"))

while number > 9:
  sum = 0
  while number > 0:
    sum += number%10
    number = number//10
  number = sum

print(sum)
