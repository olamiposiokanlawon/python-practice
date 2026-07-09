account_number= int(input("enter account number: "))
beginning_balance= int(input("enter beginning balance: "))
charges= int(input("enter charges: "))
credit= int(input("enter credit: "))
credit_limit=  int(input("enter credit limit: "))

new_balance= beginning_balance + charges - credit
print("new_balance= ", new_balance)

new_balance= beginning_balance> credit_limit
print("credit limit exceeded")