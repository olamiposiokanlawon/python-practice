def calculate_tax(earnings):
 if earnings <= 30000:
  tax= earnings * 0.15
 else:
    Tax = (30000 * 0.15) + ((Earnings - 30000) * 0.20)

 return tax

for i in range(3):
  name = input("enter citizens name: " )
  earnings= int (input("enter citizens earnings: "))
  tax= calculate_tax(earnings)
  print("name: ", name)
  print("total tax: ", tax)		