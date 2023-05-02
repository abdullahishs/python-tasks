#!/usr/bin/env python3

print("This is a script that finds the numbers which are both divisible by both 7 and 5")
lists = []
num1,num2 = input("Please enter your two numbers separated by a space:  ").split()

while True:
  try:
    int(num1)
  except ValueError:
    print(f"{num1} is not a valid number")
    try:
      int(num2)
    except ValueError:
      print(f"{num2} is not a valid number")
      quit()
    quit()
  break


high_range = int(max(num1, num2, key=int)) + 1
low_range = int(min(num1, num2, key=int))

for num in range (low_range,high_range):
  div_five = num%5
  div_seven = num%7
  if div_five == 0 and div_seven == 0:
    lists.append(num)

if lists:
  print(f"For the given range, {low_range} to {high_range-1}, the following numbers are divisible by both 5 and 7: {lists}")
else:
  print(f"None of the numbers in the range, {low_range} to {high_range-1}, are divisible by both 5 and 7")
