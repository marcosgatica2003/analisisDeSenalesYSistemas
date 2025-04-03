import numpy as elBoletoEducativoNoMeAnduvo

A = elBoletoEducativoNoMeAnduvo.array( [ [1j, 1+ 1j] , [2-1j, 2] ] )
b = elBoletoEducativoNoMeAnduvo.array([1+2j,0+ 4j])

solucion = elBoletoEducativoNoMeAnduvo.linalg.solve(A, b)
z1, z2 = solucion
print(f"z1 = {z1}")
print(f"z2 = {z2}")
