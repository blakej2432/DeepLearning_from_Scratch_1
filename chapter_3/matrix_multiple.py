#%%
import numpy as np

# %%
A = np.array([1, 2, 3, 4])
print(A)

np.ndim(A)

A.shape
A.shape[0]
# %%
B = np.array([[1,2], [3,4], [5,6]])
print(B)
np.ndim(B)
B.shape
# %%
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

np.dot(A, B)

# %%
X = np.array([1, 2])

W = np.array([[1,3,5],[2,4,6]])

Y = np.dot(X, W)
# %%
Y
# %%
