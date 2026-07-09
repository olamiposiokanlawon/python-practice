total_sales = 0

number_of_items= int(input("how many items were sold?: "))
for i in range(Number_of_items):
    item = int(input("Enter item number: "))

    if item == 1:
        total_sales += 239.99
    elif item == 2:
        total_sales += 129.75
    elif item == 3:
        total_sales += 99.95
    elif item == 4:
        total_sales += 350.89


earnings = 200 + (0.09 * total_sales)

print("Earnings = $", earnings)