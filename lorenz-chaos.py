import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Line3DCollection
import numpy as np

def lorenz(x, y, z, sigma, rho, beta):
    # Compute derivatives
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z

    return dx, dy, dz

# Parameters
sigma = 10
rho = 28
beta = 8 / 3

# Initial conditions
x, y, z = 1.0, 1.0, 1.0
dt = 0.01
steps = 10000

# RK4 Implementation
trajectory = []
for _ in range(steps):
    dx1, dy1, dz1 = lorenz(x, y, z, sigma, rho, beta)
    kx1, ky1, kz1 = dx1 * dt, dy1 * dt, dz1 * dt
    
    dx2, dy2, dz2 = lorenz(x + kx1/2, y + ky1/2, z + kz1/2, sigma, rho, beta)
    kx2, ky2, kz2 = dx2 * dt, dy2 * dt, dz2 * dt

    dx3, dy3, dz3 = lorenz(x + kx2/2, y + ky2/2, z + kz2/2, sigma, rho, beta)
    kx3, ky3, kz3 = dx3 * dt, dy3 * dt, dz3 * dt

    dx4, dy4, dz4 = lorenz(x + kx3, y + ky3, z + kz3, sigma, rho, beta)
    kx4, ky4, kz4 = dx4 * dt, dy4 * dt, dz4 * dt

    x += (kx1 + 2 * kx2 + 2 * kx3 + kx4) / 6
    y += (ky1 + 2 * ky2 + 2 * ky3 + ky4) / 6
    z += (kz1 + 2 * kz2 + 2 * kz3 + kz4) / 6

    trajectory.append((x, y, z))

# Convert trajectory to arrays
trajectory = np.array(trajectory)
xs, ys, zs = trajectory[:, 0], trajectory[:, 1], trajectory[:, 2]

# Create segments for Line3DCollection
points = np.array([xs, ys, zs]).T.reshape(-1, 1, 3)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

colors = plt.cm.cool(np.linspace(0, 1, len(segments)))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
lc = Line3DCollection(segments, colors=colors, linewidth=0.5)
ax.add_collection(lc)

ax.set_xlim(xs.min(), xs.max())
ax.set_ylim(ys.min(), ys.max())
ax.set_zlim(zs.min(), zs.max())
ax.set_title("Lorenz Attractor with Gradient Colors")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()