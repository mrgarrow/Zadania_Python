import numpy as np
# Zadanie 1
v1 = np.array([5, -1, 5])
v2 = np.array([3, 1, 0])

v3 = np.dot(v1,v2)
print(v3)

# Zadanie 2

v1 = np.array([1, 0, 0])
v2 = np.array([0, 1, 0])

v3 = np.dot(v1,v2)
rad = np.arccos(v3)
print(f'Kąt pomiędzy v1 i v2 w radianach to: {rad}')

# Zadanie 3

A1 = np.array([[2, 3], [-1, 4], [-5, 2]]) 
A2 = np.array([[4, 3, -1], [2, 0, 1]])

matrix = np.matmul(A1,A2)
determin = np.linalg.det(matrix)
print(f'Macierz w postaci 3x3 to:\n{matrix}\nA wyznacznik wynosi: {determin}')

# Zadanie 4

A = np.array([4, 3, 5, 5, 3, 5, 2, 6, 5, 2, 0, 8])
print('Unikalne wartości tablicy to:',np.unique(A))

# Zadanie 5

A = np.array([[5, -3], [1, -2]])
B = np.array([21, 7])

sol = np.linalg.solve(A,B)
print(f'Dla zadanego układu równań:\nx = {sol[0]}\ny = {sol[1]}')

