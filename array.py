import numpy as np
Array_one =np.ones(5)
print(Array_one)

Name_Emp = ['Ram','Radha','Hari']
Array_two = np.array(Name_Emp)
print(Array_two)
print(type(Array_two))

Array_Range = np.arange(8)
print(Array_Range)

Array_Reshaped = Array_Range.reshape(4,2)
print(Array_Reshaped)