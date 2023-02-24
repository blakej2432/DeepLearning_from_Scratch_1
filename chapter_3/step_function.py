import numpy as np

# x로 실수값만 받을 수 있는 계단함수
def step_function(x):
    if x > 0:
        return 1
    else:
        return 0

# np.array()를 x로 받을 수 있는 계단함수

x = np.array([-1.0, 1.0, 2.0])
x
y = x > 0
y.astype('int')

def step_function(x):
    y = x > 0
    return y.astype('int')

step_function(x)