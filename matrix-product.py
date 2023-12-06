import numpy as np

# Meminta input untuk matriks A
rows_A = int(input("Masukkan jumlah baris matriks A: "))
cols_A = int(input("Masukkan jumlah kolom matriks A: "))
print("Masukkan elemen matriks A (per baris):")
A = np.array([list(map(float, input().split())) for _ in range(rows_A)])

# Meminta input untuk matriks B
rows_B = int(input("Masukkan jumlah baris matriks B: "))
cols_B = int(input("Masukkan jumlah kolom matriks B: "))
print("Masukkan elemen matriks B (per baris):")
B = np.array([list(map(float, input().split())) for _ in range(rows_B)])

# Melakukan perkalian matriks
try:
    C = np.dot(A, B)
    print("\nHasil perkalian matriks A dan B:")
    print(C)
except ValueError:
    print("Perkalian matriks tidak dapat dilakukan karena jumlah kolom matriks A tidak sama dengan jumlah baris matriks B.")
