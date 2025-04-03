import numpy as manolo

# Esta es la matriz de coeficientes
A = manolo.array([ [1j, -1j], [-1, 1 + 1j] ])

# Vector términos independientes
b = manolo.array([2+10j, 3 -5j])

solucion = manolo.linalg.solve(A, b)
z_1, z_2 = solucion

print(f"z_1 = {z_1}")
print(f"z_2 = {z_2}")
