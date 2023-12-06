import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Fungsi untuk plot titik dan vektor
def plot_point(ax, point, color, label):
    ax.quiver(0, 0, point[0], point[1], angles='xy', scale_units='xy', scale=1, color=color, label=label)

# Transformasi matriks untuk translasi
def translation_matrix(dx, dy):
    return np.array([[1, 0, dx],
                     [0, 1, dy],
                     [0, 0, 1]])

# Transformasi matriks untuk rotasi (dalam radian)
def rotation_matrix(theta):
    return np.array([[np.cos(theta), -np.sin(theta), 0],
                     [np.sin(theta), np.cos(theta), 0],
                     [0, 0, 1]])

# Transformasi matriks untuk scaling
def scaling_matrix(sx, sy):
    return np.array([[sx, 0, 0],
                     [0, sy, 0],
                     [0, 0, 1]])

# Poin awal (matriks identitas)
point = np.array([1, 2, 1])  # Untuk transformasi 2D, hilangkan komponen Z (3x1 menjadi 2x1)

# Set up plot
fig = plt.figure(figsize=(12, 4))

# Plot poin awal
ax1 = fig.add_subplot(131)
ax1.set_title('Point Before Transformation')
plot_point(ax1, point[:2], 'b', 'Point')

# Translasi
translated_point = translation_matrix(2, 1) @ point
ax2 = fig.add_subplot(132)
ax2.set_title('After Translation')
plot_point(ax2, point[:2], 'b', 'Original Point')
plot_point(ax2, translated_point[:2], 'r', 'Translated Point')

# Rotasi
rotated_point = rotation_matrix(np.radians(45)) @ point
ax3 = fig.add_subplot(133)
ax3.set_title('After Rotation')
plot_point(ax3, point[:2], 'b', 'Original Point')
plot_point(ax3, rotated_point[:2], 'g', 'Rotated Point')

plt.tight_layout()
plt.show()
