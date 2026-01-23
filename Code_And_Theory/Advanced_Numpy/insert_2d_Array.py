import numpy as np

arr_2d = np.array([[10, 20], [30, 40]])
print(arr_2d)

# insert a new row at index 1
new_arr_2d = np.insert(arr_2d, 4, [50, 60], axis=None)
print(new_arr_2d)