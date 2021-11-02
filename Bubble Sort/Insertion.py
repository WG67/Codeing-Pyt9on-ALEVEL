import numpy

from numpy import random

x=random.randint(100, size=int(input("please input the number: ")))

print(x)
n = len(x)
for index in range(1, n):
  current = x[index]
  index2 = index
  print(x)
  while index2 > 0 and x[index2 -1] > current:
    x[index2] = x[index2 -1]
    index2 = index2 - 1
  x[index2] = current
print(x)