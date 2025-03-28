#Yael estuvo aquí

import matplotlib.pyplot as plt

z1 = 2 + 4j
z1Conjugado = z1.conjugate()

plt.text(z1.real, z1.imag, f"({z1.real}; {z1.imag})", fontsize=12)
plt.text(z1Conjugado.real, z1Conjugado.imag, f"({z1Conjugado.real}; {z1Conjugado.imag})", fontsize=12)
plt.text(5, 5, "z1 conjugado", fontsize=14)

plt.quiver(0, 0, z1.real, z1.imag, angles='xy', scale_units='xy', scale=1, color='r')

plt.quiver(0, 0, z1Conjugado.real, z1Conjugado.imag, angles='xy', scale_units='xy', scale=1, color='b')

plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.xlim(-5, 10)
plt.ylim(-5, 15)
plt.title("Ejercicio 1")
plt.grid()
plt.show()
