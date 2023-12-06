import numpy as np
import matplotlib.pyplot as plt

# Matriks koordinat segitiga
triangle = np.array([[1, 3, 2],
                     [1, 1, 3],
                     [1, 1, 1]])

# Fungsi untuk melakukan transformasi geometris
def geometric_transform(matrix, transformation_matrix):
    return np.dot(transformation_matrix, matrix)

# Translasi (geser) sebesar (2, 3)
translation_matrix = np.array([[1, 0, 2],
                               [0, 1, 3],
                               [0, 0, 1]])

# Rotasi sebesar 45 derajat
theta = np.radians(45)
rotation_matrix = np.array([[np.cos(theta), -np.sin(theta), 0],
                            [np.sin(theta), np.cos(theta), 0],
                            [0, 0, 1]])

# Penskalaan sebesar (2, 2)
scaling_matrix = np.array([[2, 0, 0],
                           [0, 2, 0],
                           [0, 0, 1]])

# Transformasi geometris
triangle_translated = geometric_transform(triangle, translation_matrix)
triangle_rotated = geometric_transform(triangle, rotation_matrix)
triangle_scaled = geometric_transform(triangle, scaling_matrix)

# Visualisasi
plt.figure(figsize=(10, 6))

# Segitiga asli
plt.subplot(231)
plt.plot(triangle[0, :], triangle[1, :], 'bo-')
plt.title('Segitiga Asli')

# Translasi
plt.subplot(232)
plt.plot(triangle_translated[0, :], triangle_translated[1, :], 'ro-')
plt.title('Setelah Translasi')

# Rotasi
plt.subplot(233)
plt.plot(triangle_rotated[0, :], triangle_rotated[1, :], 'go-')
plt.title('Setelah Rotasi')

# Penskalaan
plt.subplot(234)
plt.plot(triangle_scaled[0, :], triangle_scaled[1, :], 'co-')
plt.title('Setelah Penskalaan')

# Semua transformasi
plt.subplot(235)
plt.plot(triangle[0, :], triangle[1, :], 'bo-')
plt.plot(triangle_translated[0, :], triangle_translated[1, :], 'ro-')
plt.plot(triangle_rotated[0, :], triangle_rotated[1, :], 'go-')
plt.plot(triangle_scaled[0, :], triangle_scaled[1, :], 'co-')
plt.title('Semua Transformasi')

plt.tight_layout()
plt.show()
