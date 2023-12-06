import numpy as np
import matplotlib.pyplot as plt

# Matriks A dan B
A = np.array([[2, 1], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# 1. Penjumlahan Matriks
C_sum = A + B

# 2. Perkalian Matriks
C_mul = np.dot(A, B)

# 3. Transpos Matriks
A_transpose = np.transpose(A)
B_transpose = np.transpose(B)

# 4. Identitas dan Matriks
I = np.identity(2)
IA = np.dot(I, A)
AI = np.dot(A, I)

# Visualisasi
fig, axs = plt.subplots(2, 3, figsize=(12, 8))

# Plotting matriks A
axs[0, 0].imshow(A, cmap='viridis', vmin=0, vmax=8)
axs[0, 0].set_title('Matriks A')

# Plotting matriks B
axs[0, 1].imshow(B, cmap='viridis', vmin=0, vmax=8)
axs[0, 1].set_title('Matriks B')

# Plotting hasil penjumlahan matriks
axs[0, 2].imshow(C_sum, cmap='viridis', vmin=0, vmax=20)
axs[0, 2].set_title('A + B')

# Plotting hasil perkalian matriks
axs[1, 0].imshow(C_mul, cmap='viridis', vmin=0, vmax=60)
axs[1, 0].set_title('A * B')

# Plotting transpos matriks A
axs[1, 1].imshow(A_transpose, cmap='viridis', vmin=0, vmax=8)
axs[1, 1].set_title('A^T')

# Plotting transpos matriks B
axs[1, 2].imshow(B_transpose, cmap='viridis', vmin=0, vmax=8)
axs[1, 2].set_title('B^T')

# Menyembunyikan sumbu
for ax in axs.flat:
    ax.axis('off')

plt.tight_layout()
plt.show()
