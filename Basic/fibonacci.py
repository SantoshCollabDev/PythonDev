term1 = 1
term2 = 2
new_term = 0
index = 4000000
sum_even_term = 0

new_term = term1
while new_term < index:
  print(new_term)
  if new_term%2 == 0:
    sum_even_term += new_term
  term1 = term2
  term2 += new_term
  new_term = term1

print(f"Sum of Even Terms is {sum_even_term}")
