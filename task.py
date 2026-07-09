list1 = [1, 2, 3]
list2 = [4, 5, 6]

list3 = list1 + list2

print(list3)

def secondLargest(numbers):
    numbers = list(set(numbers))
    numbers.sort()
    return numbers[-2]

print(secondLargest([10, 10, 9]))