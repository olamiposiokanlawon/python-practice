score = int(input("enter student score"))
if score < 0 or score > 100:
print("invalid score")

elif score>=90:
print("grade A")

elif score>=80:
print("grade B")

elif score>=70:
print("grade C")

elif score>=60:
print("grade D")

else:
print("grade F")
