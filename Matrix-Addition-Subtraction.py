import numpy as np

def input_matrix():
    rows = int(input("Masukkan jumlah baris matriks: "))
    cols = int(input("Masukkan jumlah kolom matriks: "))
    
    matrix = np.zeros((rows, cols))
    
    print("Masukkan elemen-elemen matriks:")
    for i in range(rows):
        for j in range(cols):
            matrix[i, j] = float(input(f"Elemen [{i+1},{j+1}]: "))
    
    return matrix

def matrix_addition(matrix1, matrix2):
    return matrix1 + matrix2

def matrix_subtraction(matrix1, matrix2):
    return matrix1 - matrix2

# Input matriks pertama
print("Masukkan matriks pertama:")
matrix_A = input_matrix()

# Input matriks kedua
print("\nMasukkan matriks kedua:")
matrix_B = input_matrix()

# Pilihan operasi
operation = input("Pilih operasi (1. Pertambahan, 2. Pengurangan): ")

if operation == '1':
    result = matrix_addition(matrix_A, matrix_B)
    operation_name = 'Pertambahan'
elif operation == '2':
    result = matrix_subtraction(matrix_A, matrix_B)
    operation_name = 'Pengurangan'
else:
    print("Operasi tidak valid.")
    result = None

# Menampilkan hasil
if result is not None:
    print(f"\nHasil {operation_name} matriks:")
    print(result)
