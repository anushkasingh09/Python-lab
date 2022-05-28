import numpy as np
arr = np.array([(1,2,3,4),(9,8,7,6)])
print("Initial shape:",arr.shape)
arr=arr.reshape(4,2)
print("Shape after reshaping:",arr.shape)
