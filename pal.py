num = int(input("Enter a 5-digit integer: "))

digit1 = num // 10000
digit2 = (num // 1000) % 10
digit3 = (num // 100) % 10
digit4 = (num // 10) % 10
digit5 = num % 10

if digit1 == digit5 and digit2 == digit4:
 print(num, "is a palindrome")
else:
 print(num, "is not a palindrome")