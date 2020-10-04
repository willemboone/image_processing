import cv2
import numpy as np
import matplotlib.pyplot as plt

"""
this script shows what erosion and dilation are
based on opencv
"""

# create some random data
v = np.random.randint(0, 2, (100, 100), 'uint8')
w = np.random.randint(0, 2, (100, 100), 'uint8')
x = np.random.randint(0, 2, (100, 100), 'uint8')
y = np.random.randint(0, 2, (100, 100), 'uint8')
z = np.random.randint(0, 2, (100, 100), 'uint8')
data_0 = v * w * x * y * z

# create some structured data
data_1 = np.zeros((100, 100), 'uint8')
data_1[25:75, 25:75] = 1
data_1 = data_1 + (v * w * z)
data_1 = data_1 - (x * y * z)
data_1[data_1 > 1] = 1
data_1[data_1 < 0] = 0

# create kernel for dilation and erosion
# this numpy kernel is just a square
# kernel = np.ones((5, 5), 'uint8')

# the cv2.MORPH_ELLIPSE has a weird not really elliptical shape
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (6, 6))

# manually defined kernel seems best solution
dilate_kernel = np.array(([0, 1, 1, 1, 0], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [0, 1, 1, 1, 0]), 'uint8')
erode_kernel = np.ones((3, 3))

# erode
eroded_0 = cv2.erode(data_0, erode_kernel)
eroded_1 = cv2.erode(data_1, erode_kernel)

# dilate
dilated_0 = cv2.dilate(data_0, kernel=dilate_kernel, iterations=1)
dilated_1 = cv2.dilate(data_1, kernel=dilate_kernel, iterations=1)

# erode + dilate
proc_0 = cv2.dilate(cv2.erode(data_0, erode_kernel), dilate_kernel, iterations=1)
proc_1 = cv2.dilate(cv2.erode(data_1, erode_kernel), dilate_kernel, iterations=5)

# plot
cmap = 'Greys'
fig, axes = plt.subplots(2, 4)
axes[0, 0].imshow(data_0, cmap=cmap, vmin=0, vmax=1)
axes[0, 1].imshow(eroded_0, cmap=cmap, vmin=0, vmax=1)
axes[0, 2].imshow(dilated_0, cmap=cmap, vmin=0, vmax=1)
axes[0, 3].imshow(proc_0, cmap=cmap, vmin=0, vmax=1)

axes[1, 0].imshow(data_1, cmap=cmap, vmin=0, vmax=1)
axes[1, 1].imshow(eroded_1, cmap=cmap, vmin=0, vmax=1)
axes[1, 2].imshow(dilated_1, cmap=cmap, vmin=0, vmax=1)
axes[1, 3].imshow(proc_1, cmap=cmap, vmin=0, vmax=1)

for i in range(2):
    axes[i, 0].set_title("original")
    axes[i, 1].set_title("erosion")
    axes[i, 2].set_title("dilation")
    axes[i, 3].set_title("erosion + dilation")

plt.show()

