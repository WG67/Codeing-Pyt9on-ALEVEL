# Python program for implementation of Bubble Sort

def bubbleSort(x):
	n = len(x)


	for i in range(n-1):



		for j in range(0, n-i-1):


			if x[j] > x[j + 1] :
				x[j], x[j + 1] = x[j + 1], x[j]
from numpy import random

x=random.randint(100, size=int(input("please input the number")))

print(x)
bubbleSort(x)
print ("Sorted array is:")
for i in range(len(x)):
	print ("% d" % x[i]),
