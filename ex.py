passes = 0
failures = 0
student_counter = 0

while student_counter < 10:
 valid_input = False
    
 while valid_input == False:
  result = int(input('Enter result (1 = pass, 2 = fail): '))
 if result == 1:
  valid_input = True
 if result == 2:
  valid_input = True
            
 if valid_input == False:
  print('Invalid input. Please enter 1 or 2.')

 if result == 1:
  passes = passes + 1
  else:
  failures = failures + 1
        
 student_counter = student_counter + 1

print('Passed:', passes)
print('Failed:', failures)