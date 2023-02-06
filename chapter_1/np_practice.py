import numpy as np

x = np.array([1.0, 2.0, 3.0])

print(x)
type(x)

x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])

x + y # 원소별 덧셈
x * y # 원소별 곱셈
x / y

x / 2.0 # 스칼라를 분배법칙 -> 브로드캐스트

A = np.array([[1, 2], [3, 4]])
print(A)

A.shape
A.dtype

B = np.array([[3, 0], [0, 6]])
print(B)

A + B
A * B # 원소 곱
A @ B # 행렬 곱

# 브로드 캐스트의 예

A = np.array([[1, 2],[3, 4]])
B = np.array([10, 20]) # -> 2차원으로 복제해서 연산 실행

A * B

X = np.array([[51, 55], [14, 19], [0, 4]])
X.flatten()

X[np.array([0,2])]

X > 15
X[X > 15]
