#create an image 
import matplotlib.pyplot as plt
import numpy as np

# Create a new figure
fig, ax = plt.subplots()

# 1. Circle
circle = plt.Circle((0.5, 0.5), 0.2, color='blue', alpha=0.5)  # center at (0.5, 0.5), radius 0.2
ax.add_artist(circle)

# 2. Rectangle
rectangle = plt.Rectangle((0.1, 0.1), 0.3, 0.4, color='green', alpha=0.5)  # bottom-left corner at (0.1, 0.1), width 0.3, height 0.4
ax.add_artist(rectangle)

# 3. Polygon (Triangle)
triangle = plt.Polygon([[0.7, 0.1], [0.9, 0.4], [0.6, 0.4]], color='red', alpha=0.5)  # vertices of the triangle
ax.add_artist(triangle)

# 4. Line
x = np.linspace(0, 1, 100)
y = 0.5 * np.sin(2 * np.pi * x) + 0.5
ax.plot(x, y, color='black', label='Sine Wave')

# Set limits and aspect
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal', adjustable='box')

# Add a legend
ax.legend()

# Title
plt.title('Shapes in Matplotlib')

# Show the plot
plt.grid()
plt.show()
