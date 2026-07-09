def rearrange(array):
  for i in range(1):
      first=array[0]
      array[0] = array[-1]
      array[-1] = first

  return array

numbers = [ 1,5,6,2,3,8,4]
print(rearrange(numbers))