import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Définition des fonctions
def f1(x, y):
    return np.exp(x) * np.cos(y)

def f2(x, y):
    return (x - y)/(1 + x**2 + y**2)

def f3(x, y):
    return np.sin(x) - np.sin(y)

# Grille de valeurs
x = np.linspace(-10, 10, 400)
y = np.linspace(-10, 10, 400)
x, y = np.meshgrid(x, y)

# Calcul des fonctions sur les grilles
z1 = f1(x, y)
z2 = f2(x, y)
z3 = f3(x, y)

fig = plt.figure(figsize=(18, 12))

# f1
ax1 = fig.add_subplot(231, projection='3d')
ax1.plot_surface(x, y, z1, cmap='viridis')
ax1.title.set_text('f1')

ax4 = fig.add_subplot(234)
contour1 = ax4.contour(x, y, z1, 20, cmap='viridis')
ax4.clabel(contour1, inline=True, fontsize=8)
ax4.title.set_text('Courbes de niveau de f1')

# f2
ax2 = fig.add_subplot(232, projection='3d')
ax2.plot_surface(x, y, z2, cmap='magma')
ax2.title.set_text('f2')

ax5 = fig.add_subplot(235)
contour2 = ax5.contour(x, y, z2, 20, cmap='magma')
ax5.clabel(contour2, inline=True, fontsize=8)
ax5.title.set_text('Courbes de niveau de f2')

# f3
ax3 = fig.add_subplot(233, projection='3d')
ax3.plot_surface(x, y, z3, cmap='plasma')
ax3.title.set_text('f3')

ax6 = fig.add_subplot(236)
contour3 = ax6.contour(x, y, z3, 20, cmap='plasma')
ax6.clabel(contour3, inline=True, fontsize=8)
ax6.title.set_text('Courbes de niveau de f3')

plt.tight_layout()
plt.show()
