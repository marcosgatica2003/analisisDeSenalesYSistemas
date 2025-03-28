import matplotlib.pyplot as plt


def vectorComplejo(z, color):
    plt.quiver(0, 0, z.real, z.imag, angles='xy', scale_units='xy', scale=1, color=f'{color}')
    plt.text(z.real, z.imag, f"({z.real};{z.imag})", fontsize=12)

z = 2 - 3j
reciprocoZ = z**(-1)
vectorComplejo(z, 'r')
vectorComplejo(reciprocoZ, 'b')

plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.xlim(-3, 3)
plt.ylim(-3, 4)
plt.grid()
plt.title("Ejercicio 3", fontsize=12)
plt.show()

