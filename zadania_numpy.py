import numpy as np

# Zadanie 1

A = np.array([[3, 2, 1, 4], [5, 2, 1, 6]])
B = np.array([[3, 2, 1, 4],
 [5, 2, 0, 6]])
C = np.array([[True, False, False],
 [True, True, True]])
D = np.array([0.1, 0.3],)
print('Wynik:')
print('A:',np.all(A))
print('B:',np.all(B))
print('C:',np.all(C))
print('D:',np.all(D))
