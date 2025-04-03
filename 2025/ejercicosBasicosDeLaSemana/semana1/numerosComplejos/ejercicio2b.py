import matplotlib.pyplot as plt


def vectorComplejo(z, color):
    plt.quiver(0, 0, z.real, z.imag, angles='xy', scale_units='xy', scale=1, color=f'{color}')
    plt.text(z.real, z.imag, f"({z.real};{z.imag})", fontsize=12)

z1 = 2 - 3j
z2 = 4 + 6j
z3 = z1 - z2

vectorComplejo(z1, 'r')
vectorComplejo(z2, 'b')
vectorComplejo(z3, 'g')

plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.xlim(-5, 7)
plt.ylim(-10, 10)
plt.grid()
plt.title("Ejercicio 2", fontsize=12)
plt.show()
