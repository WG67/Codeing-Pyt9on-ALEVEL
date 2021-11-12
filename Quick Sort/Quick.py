def partition(array, low, high):
  # choose the rightmost element as pivot
  pivot = array[high]
  # pointer for greater element
  i = low - 1  
  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])
  (array[i + 1], array[high]) = (array[high], array[i + 1])
  return i + 1

def quickSort(array, low, high):
  if low < high:
    pi = partition(array, low, high)
    quickSort(array, low, pi - 1)
    quickSort(array, pi + 1, high)

# creating an empty list

# number of elements as input

 
# iterating till the range
import random

x = random.randint(100, size =int(input("please input the number")))

print(x)

#sorts the user inputted Array

size = len(x)

quickSort(x, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(x)
    
    
  
    
  
  

  

