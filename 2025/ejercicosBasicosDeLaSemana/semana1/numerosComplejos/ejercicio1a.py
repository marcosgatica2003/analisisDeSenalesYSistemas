#Yael estuvo aquí

import matplotlib.pyplot as plt

z1 = 2 + 4j
z2 = -3 + 8j
z3 = z1 + z2

x_vals = [0, z1.real, z3.real]
y_vals = [0, z1.imag, z3.imag]

plt.scatter([z1.real, z2.real, z3.real], [z1.imag, z2.imag, z3.imag], color=['r', 'b', 'g'])
plt.text(z1.real, z1.imag, "z1", fontsize=12)
plt.text(z2.real, z2.imag, "z2", fontsize=12)
plt.text(z3.real, z3.imag, "z2+z1", fontsize=12)

plt.quiver(0, 0, z1.real, z1.imag, angles='xy', scale_units='xy', scale=1, color='r')
plt.quiver(z1.real, z1.imag, z2.real, z2.imag, angles='xy', scale_units='xy', scale=1, color='b')
plt.quiver(0, 0, z3.real, z3.imag, angles='xy', scale_units='xy', scale=1, color='g')
plt.quiver(0, 0, z2.real, z2.imag, angles='xy', scale_units='xy', scale=1, color='b')

plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.xlim(-5, 5)
plt.ylim(-5, 15)
plt.title("Ejercico 1")
plt.grid()
plt.show()
