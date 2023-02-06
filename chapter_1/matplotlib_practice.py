#%%
# -> # %% 넣으면 jupyter 셀처럼. 그리고 pip install ipykernel 넣으면 그래프 볼 수 있음
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 6, 0.1)
y = np.sin(x)
y

plt.plot(x, y)
plt.show()
#%%

x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

# 그리기

plt.plot(x, y1, label='sin')
plt.plot(x, y2, linestyle='--', label='cos')
plt.xlabel("x")
plt.ylabel('y')
plt.title('sin & cos')
plt.legend()
plt.show()



# %%
import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('electra_graph.png') # 왜 안될까

plt.imshow(img)
plt.show()
# %%
import os
os.getcwd()
# %%
