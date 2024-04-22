import random
rand_gen_num = random.randint(1,100)
print(rand_gen_num)

user_won = False
for chance in range(1,7):
  user_guess_num = int(input("Enter a number between 1 to 100"))
  if user_guess_num < rand_gen_num:
    print("Your number < number to be guessed")
  elif user_guess_num > rand_gen_num:
    print("Your number > number to be guessed")
  else:
    print("Awesome !! You have WON")
    user_won = True
    break

if not user_won:
  print(" Better Luck Next Time!")