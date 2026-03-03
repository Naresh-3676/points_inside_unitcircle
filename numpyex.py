import numpy as np
# a=np.array([1,2,3,4,5,4,7,7,8,6,8,8,9,9,9,21,9,12])

# a=np.zeros((5,5))

# a=np.eye((3))
# print(a)

# a=np.random.randint(1,10,(5,2))
# print(a)

# a=np.random.rand(1,10)
# print(a)

#-->mean 0 std 1
# a=np.random.uniform(1,110,(5,5))
# print(a)

#means 0 std 1
# a=np.random.normal(0,1,(5,5))
# print(a)

#-->produces same random numbers every time
# np.random.seed(54)
# a=np.random.rand(5,5)
# print(a)
# np.random.seed(54)
# b=np.random.rand(5,5)
# print(b)

# a=np.arange(30)
# b=a[::2]
# c=a[5:16]

# a=np.random.randint(1,50,(4,4))
# print(a)
# #the first row
# b=a[0:1]
# print(b)

#  the last column
# c=a[1:3,1:3]
# print(c)

# a=np.arange(9).reshape(3,3)
# print(a)

 
# print(np.sum(a))
# print(np.mean(a))
# print(np.std(a))
# print(np.min(a))
# print(np.max(a))


a=np.random.randint(1,100,(1,20))
# print(a)
# #values >50

# b=a[a>50]
# print(b)


# #counting the numbers
# c=np.count_nonzero(a[(a>30) & (a<70)])
# print(c)

# #replacing odd nubers with -1
# d=a.copy()
# d[d%2!=0]=-1
# print(d)

# a=np.arange(1,10).reshape(3,3)
# b=np.arange(1,10).reshape(3,3)
# print(a)
# print(b)
# print(a*b)
# print(a+b)
# print(np.linalg.det(a))
# print(np.linalg.det(b))
# c=np.array([45,7,88,8,8,87,6,5,76])
# d=c.reshape(3,3)
# print(np.linalg.det(d))
# print(np.linalg.inv(d))


#reshaping and stacking
# a=np.arange(24).reshape(3,8)
# b=np.arange(24).reshape(3,8)
# print(a)
# print(np.hsplit(a,2))
# print(np.vstack((a,b)))

# a=np.array([[1,2,3],[4,5,6]])
# b=np.array([10,20,30])
# print(a+b)
# print(a*b)

# vectorization

# def classify(x):
#     return 0 if x<50 else 1
# vfunc=np.vectorize(classify)

# a=np.random.randint(1,100,25)
# print("actual array:",a)
# print("vectoraized array:",vfunc(a))

print("="*60)
print("NUMPY ATTRIBUTES AND FUNCTIONS DEMONSTRATION")
print("="*60)

# # 1. ARRAY CREATION
# print("\n1. ARRAY CREATION")
# print("-"*40)
# a = np.array([1, 2, 3, 4, 5])
# print(f"Basic array: {a}")

# zeros = np.zeros((2, 3))
# print(f"Zeros array:\n{zeros}")

# ones = np.ones((2, 3))
# print(f"Ones array:\n{ones}")

# empty = np.empty((2, 2))
# print(f"Empty array:\n{empty}")

# full = np.full((2, 3), 7)
# print(f"Full array (filled with 7):\n{full}")

# # 2. RANGE AND SEQUENCE
# print("\n2. RANGE AND SEQUENCE")
# print("-"*40)
# arange_arr = np.arange(0, 10, 2)
# print(f"arange(0, 10, 2): {arange_arr}")

# linspace_arr = np.linspace(0, 10, 5)
# print(f"linspace(0, 10, 5): {linspace_arr}")

# logspace_arr = np.logspace(0, 2, 3)
# print(f"logspace(0, 2, 3): {logspace_arr}")

# # 3. IDENTITY AND DIAGONAL
# print("\n3. IDENTITY AND DIAGONAL")
# print("-"*40)
# identity = np.eye(3)
# print(f"Identity matrix:\n{identity}")

# diag_arr = np.diag([1, 2, 3, 4])
# print(f"Diagonal matrix:\n{diag_arr}")

# # 4. RANDOM NUMBERS
# print("\n4. RANDOM NUMBERS")
# print("-"*40)
# np.random.seed(42)
# rand_normal = np.random.normal(0, 1, 5)
# print(f"Normal distribution: {rand_normal}")

# rand_uniform = np.random.uniform(0, 10, 5)
# print(f"Uniform distribution: {rand_uniform}")

# rand_choice = np.random.choice([1, 2, 3, 4, 5], 5)
# print(f"Random choice: {rand_choice}")

# rand_shuffle = np.arange(10)
# np.random.shuffle(rand_shuffle)
# print(f"Shuffled array: {rand_shuffle}")

# # 5. ARRAY ATTRIBUTES
# print("\n5. ARRAY ATTRIBUTES")
# print("-"*40)
# arr = np.arange(24).reshape(2, 3, 4)
# print(f"Shape: {arr.shape}")
# print(f"Size: {arr.size}")
# print(f"Ndim: {arr.ndim}")
# print(f"Dtype: {arr.dtype}")
# print(f"Itemsize: {arr.itemsize} bytes")
# print(f"Nbytes: {arr.nbytes} bytes")
# print(f"Strides: {arr.strides}")

# # 6. RESHAPE AND RESIZE
# print("\n6. RESHAPE AND RESIZE")
# print("-"*40)
# arr_reshape = np.arange(12).reshape(3, 4)
# print(f"Reshaped (3x4):\n{arr_reshape}")

# arr_flatten = arr_reshape.flatten()
# print(f"Flattened: {arr_flatten}")

# arr_ravel = arr_reshape.ravel()
# print(f"Raveled: {arr_ravel}")

# arr_transpose = arr_reshape.T
# print(f"Transposed:\n{arr_transpose}")

# # 7. SLICING AND INDEXING
# print("\n7. SLICING AND INDEXING")
# print("-"*40)
# arr = np.arange(20)
# print(f"Original: {arr}")
# print(f"arr[5]: {arr[5]}")
# print(f"arr[2:8]: {arr[2:8]}")
# print(f"arr[::3]: {arr[::3]}")
# print(f"arr[::-1]: {arr[::-1]}")

# arr_2d = np.arange(12).reshape(3, 4)
# print(f"\n2D array:\n{arr_2d}")
# print(f"arr_2d[1, 2]: {arr_2d[1, 2]}")
# print(f"arr_2d[1, :]: {arr_2d[1, :]}")
# print(f"arr_2d[:, 2]: {arr_2d[:, 2]}")

# # 8. BOOLEAN INDEXING
# print("\n8. BOOLEAN INDEXING")
# print("-"*40)
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# mask = arr > 5
# print(f"Array: {arr}")
# print(f"arr > 5: {arr[mask]}")
# print(f"arr % 2 == 0: {arr[arr % 2 == 0]}")
# print(f"(arr > 3) & (arr < 8): {arr[(arr > 3) & (arr < 8)]}")

# # 9. MATHEMATICAL OPERATIONS
# print("\n9. MATHEMATICAL OPERATIONS")
# print("-"*40)
# arr = np.array([1, 2, 3, 4, 5])
# print(f"Original: {arr}")
# print(f"Sum: {np.sum(arr)}")
# print(f"Mean: {np.mean(arr)}")
# print(f"Median: {np.median(arr)}")
# print(f"Std Dev: {np.std(arr)}")
# print(f"Variance: {np.var(arr)}")
# print(f"Min: {np.min(arr)}")
# print(f"Max: {np.max(arr)}")
# print(f"Prod: {np.prod(arr)}")
# print(f"Cumsum: {np.cumsum(arr)}")
# print(f"Cumprod: {np.cumprod(arr)}")

# # 10. ROUNDING FUNCTIONS
# print("\n10. ROUNDING FUNCTIONS")
# print("-"*40)
# arr = np.array([1.25, 2.75, 3.45, 4.99, 5.15])
# print(f"Original: {arr}")
# print(f"np.round(): {np.round(arr)}")
# print(f"np.floor(): {np.floor(arr)}")
# print(f"np.ceil(): {np.ceil(arr)}")
# print(f"np.trunc(): {np.trunc(arr)}")

# # 11. TRIGONOMETRIC FUNCTIONS
# print("\n11. TRIGONOMETRIC FUNCTIONS")
# print("-"*40)
# arr = np.array([0, np.pi/2, np.pi, 3*np.pi/2])
# print(f"Array (in radians): {arr}")
# print(f"sin: {np.sin(arr)}")
# print(f"cos: {np.cos(arr)}")
# print(f"tan: {np.tan(arr)}")
# print(f"arcsin(0.5): {np.arcsin(0.5)}")
# print(f"arccos(0): {np.arccos(0)}")
# print(f"arctan(1): {np.arctan(1)}")

# # 12. EXPONENTIAL AND LOGARITHMIC
# print("\n12. EXPONENTIAL AND LOGARITHMIC")
# print("-"*40)
# arr = np.array([1, 2, 3, 4, 5])
# print(f"Array: {arr}")
# print(f"exp: {np.exp(arr)}")
# print(f"log: {np.log(arr)}")
# print(f"log10: {np.log10(arr)}")
# print(f"sqrt: {np.sqrt(arr)}")
# print(f"power(arr, 2): {np.power(arr, 2)}")

# # 13. ABSOLUTE AND SIGN
# print("\n13. ABSOLUTE AND SIGN")
# print("-"*40)
# arr = np.array([-5, -3, 0, 3, 5])
# print(f"Array: {arr}")
# print(f"abs: {np.abs(arr)}")
# print(f"sign: {np.sign(arr)}")

# # 14. CONCATENATE AND STACK
# print("\n14. CONCATENATE AND STACK")
# print("-"*40)
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# print(f"arr1: {arr1}")
# print(f"arr2: {arr2}")
# print(f"concatenate: {np.concatenate([arr1, arr2])}")
# print(f"vstack:\n{np.vstack([arr1, arr2])}")
# print(f"hstack:\n{np.hstack([arr1, arr2])}")
# print(f"stack:\n{np.stack([arr1, arr2])}")

# # 15. REPEAT AND TILE
# print("\n15. REPEAT AND TILE")
# print("-"*40)
# arr = np.array([1, 2, 3])
# print(f"Array: {arr}")
# print(f"repeat(2): {np.repeat(arr, 2)}")
# print(f"tile(2): {np.tile(arr, 2)}")

# # 16. SORTING AND SEARCHING
# print("\n16. SORTING AND SEARCHING")
# print("-"*40)
# arr = np.array([5, 2, 8, 1, 9, 3])
# print(f"Original: {arr}")
# print(f"sort(): {np.sort(arr)}")
# print(f"argsort(): {np.argsort(arr)}")
# print(f"argmax(): {np.argmax(arr)}")
# print(f"argmin(): {np.argmin(arr)}")
# print(f"searchsorted(6): {np.searchsorted(np.sort(arr), 6)}")

# # 17. UNIQUE AND COUNT
# print("\n17. UNIQUE AND COUNT")
# print("-"*40)
# arr = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
# print(f"Array: {arr}")
# unique_vals, counts = np.unique(arr, return_counts=True)
# print(f"Unique values: {unique_vals}")
# print(f"Counts: {counts}")
# print(f"count_nonzero: {np.count_nonzero(arr > 2)}")

# # 18. COMPARISON AND LOGICAL OPERATIONS
# print("\n18. COMPARISON AND LOGICAL OPERATIONS")
# print("-"*40)
# arr1 = np.array([1, 2, 3, 4, 5])
# arr2 = np.array([2, 2, 2, 4, 6])
# print(f"arr1: {arr1}")
# print(f"arr2: {arr2}")
# print(f"arr1 == arr2: {np.equal(arr1, arr2)}")
# print(f"arr1 < arr2: {np.less(arr1, arr2)}")
# print(f"arr1 > arr2: {np.greater(arr1, arr2)}")
# print(f"all(arr1 > 0): {np.all(arr1 > 0)}")
# print(f"any(arr1 > 4): {np.any(arr1 > 4)}")

# # 19. ELEMENT-WISE OPERATIONS
# print("\n19. ELEMENT-WISE OPERATIONS")
# print("-"*40)
# arr1 = np.array([1, 2, 3, 4])
# arr2 = np.array([2, 3, 4, 5])
# print(f"arr1: {arr1}")
# print(f"arr2: {arr2}")
# print(f"arr1 + arr2: {arr1 + arr2}")
# print(f"arr1 - arr2: {arr1 - arr2}")
# print(f"arr1 * arr2: {arr1 * arr2}")
# print(f"arr1 / arr2: {arr1 / arr2}")
# print(f"arr1 ** 2: {arr1 ** 2}")
# print(f"arr1 % arr2: {arr1 % arr2}")

# # 20. LINEAR ALGEBRA
# print("\n20. LINEAR ALGEBRA")
# print("-"*40)
# A = np.array([[1, 2], [3, 4]])
# B = np.array([[5, 6], [7, 8]])
# print(f"Matrix A:\n{A}")
# print(f"Matrix B:\n{B}")
# print(f"A @ B (dot product):\n{A @ B}")
# print(f"np.dot(A, B):\n{np.dot(A, B)}")
# print(f"Determinant of A: {np.linalg.det(A)}")
# print(f"Inverse of A:\n{np.linalg.inv(A)}")
# print(f"Transpose of A:\n{A.T}")
# print(f"Rank of A: {np.linalg.matrix_rank(A)}")

# # 21. STATISTICS
# print("\n21. STATISTICS")
# print("-"*40)
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(f"Array: {arr}")
# print(f"Percentile 25: {np.percentile(arr, 25)}")
# print(f"Percentile 50: {np.percentile(arr, 50)}")
# print(f"Percentile 75: {np.percentile(arr, 75)}")
# print(f"Quantile 0.5: {np.quantile(arr, 0.5)}")

# # 22. SAVING AND LOADING
# print("\n22. SAVING AND LOADING")
# print("-"*40)
# arr = np.arange(10)
# np.save('temp_array.npy', arr)
# loaded = np.load('temp_array.npy')
# print(f"Saved and loaded array: {loaded}")

# # 23. COPY VS VIEW
# print("\n23. COPY VS VIEW")
# print("-"*40)
# original = np.array([1, 2, 3, 4, 5])
# view_arr = original.view()
# copy_arr = original.copy()
# original[0] = 999
# print(f"Original (modified): {original}")
# print(f"View (also modified): {view_arr}")
# print(f"Copy (unchanged): {copy_arr}")

# # 24. DTYPES
# print("\n24. DTYPES")
# print("-"*40)
# int_arr = np.array([1, 2, 3], dtype=np.int32)
# float_arr = np.array([1.1, 2.2, 3.3], dtype=np.float64)
# complex_arr = np.array([1+2j, 3+4j], dtype=np.complex128)
# bool_arr = np.array([True, False, True], dtype=np.bool_)
# print(f"int32: {int_arr} (dtype: {int_arr.dtype})")
# print(f"float64: {float_arr} (dtype: {float_arr.dtype})")
# print(f"complex128: {complex_arr} (dtype: {complex_arr.dtype})")
# print(f"bool: {bool_arr} (dtype: {bool_arr.dtype})")

# # 25. WHERE AND SELECT
# print("\n25. WHERE AND SELECT")
# print("-"*40)
# arr = np.array([1, 2, 3, 4, 5])
# result = np.where(arr > 3, arr*10, arr)
# print(f"Array: {arr}")
# print(f"where(arr > 3, arr*10, arr): {result}")

# # 26. SORTING ALONG AXIS
# print("\n26. SORTING ALONG AXIS")
# print("-"*40)
# arr = np.array([[3, 2, 1], [6, 5, 4], [9, 8, 7]])
# print(f"Original:\n{arr}")
# print(f"Sort along axis 0:\n{np.sort(arr, axis=0)}")
# print(f"Sort along axis 1:\n{np.sort(arr, axis=1)}")

# # 27. REDUCING OPERATIONS
# print("\n27. REDUCING OPERATIONS")
# print("-"*40)
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(f"Array:\n{arr}")
# print(f"Sum (all): {np.sum(arr)}")
# print(f"Sum (axis=0): {np.sum(arr, axis=0)}")
# print(f"Sum (axis=1): {np.sum(arr, axis=1)}")
# print(f"Mean (axis=0): {np.mean(arr, axis=0)}")
# print(f"Mean (axis=1): {np.mean(arr, axis=1)}")

# # 28. POLYNOMIAL
# print("\n28. POLYNOMIAL")
# print("-"*40)
# # Fit: y = 2x^2 + 3x + 1
# x = np.array([1, 2, 3, 4, 5])
# y = 2*x**2 + 3*x + 1
# coeffs = np.polyfit(x, y, 2)
# print(f"Polynomial coefficients: {coeffs}")
# poly = np.poly1d(coeffs)
# print(f"Polynomial: {poly}")
# print(f"Evaluate at x=6: {poly(6)}")

# # 29. VECTORIZED FUNCTION
# print("\n29. VECTORIZED FUNCTION")
# print("-"*40)
# def custom_func(x):
#     return x**2 if x > 2 else 0

# vfunc = np.vectorize(custom_func)
# arr = np.array([1, 2, 3, 4, 5])
# result = vfunc(arr)
# print(f"Array: {arr}")
# print(f"Vectorized function result: {result}")

# # 30. APPLY ALONG AXIS
# print("\n30. APPLY ALONG AXIS")
# print("-"*40)
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# result = np.apply_along_axis(np.sum, 1, arr)
# print(f"Array:\n{arr}")
# print(f"Apply sum along axis 1: {result}")

# print("\n" + "="*60)

# # ravel ->change the actual array elements 
# b=np.ravel(a)
# b[4]=24
# print(b)
# print(a)
# # flatten -> does not affect the actual array elments
# c=a.flatten()
# print(c)
# c[3]=33
# print(c)
# print(a)