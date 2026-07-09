numbers = [8,5,6,4,9,2]

smallest = numbers[0]

for num in numbers:
  if num < smallest:
     smallest = num

print("smallest number is: ", smallest)