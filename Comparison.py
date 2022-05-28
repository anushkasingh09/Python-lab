import numpy as np
import sys
list1= [1,2,3,4,5,6,7,8,9,10]
print("Size of the list:",sys.getsizeof(int)*len(list1)) 
arr= np.array([1,2,3,4,5,6,7,8,9,10])
print("Size of the array:",arr.size*arr.itemsize)
