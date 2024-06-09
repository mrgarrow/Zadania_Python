import numpy as np

# Zadanie 1

A = np.array([[3, 2, 1, 4], [5, 2, 1, 6]])
B = np.array([[3, 2, 1, 4], [5, 2, 0, 6]])
C = np.array([[True, False, False], [True, True, True]])
D = np.array([0.1, 0.3],)
print('Wynik:')
print('A:',np.all(A))
print('B:',np.all(B))
print('C:',np.all(C))
print('D:',np.all(D))

# Zadanie 2

A = np.array([[0, 0, 0], [0, 0, 0]])
B = np.array([[0, 0, 0], [0, 1, 0]])
C = np.array([[False, False, False], [True, False, False]])
D = np.array([[0.1, 0.0]])
print('Wynik:')
print('A:',np.any(A))
print('B:',np.any(B))
print('C:',np.any(C))
print('D:',np.any(D))

# Zadanie 3

A = np.array([0.4, 0.5, 0.3])
B = np.array([0.39999999, 0.5000001, 0.3])

print("Wynik: ",np.allclose(A,B))

# Zadanie 4

ArrayA = np.full((10,10),255,float)
print(ArrayA)

# Zadanie 5

A = np.array([[3, 2, 1, np.nan], [5, np.nan, 1, 6]])
B = np.isnan(A)
print('Wynik:\n',B)

# Zadanie 6

A = np.array([0.4, 0.5, 0.3, 0.9])
B = np.array([0.38, 0.51, 0.3, 0.91])

check = A > B
print('Wynik:\n',check)

# Zadanie 7

A = np.array([0.4, 0.5, 0.3])
B = np.array([0.3999999999, 0.5000000001, 0.3])
print('Wynik:')
for value in A:
    if value == value in B:
        print('True',sep=' ')
    else:
        print('False', sep=' ')

# metoda 2
compare = A == B
print('Wynik:\n',compare)