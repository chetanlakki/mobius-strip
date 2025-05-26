# mobius_strip.py
import numpy as np
import matplotlib.pyplot as plt

class MobiusStrip:
    def __init__(self, R=2, w=0.5, n=200):
        self.R = R  # Radius from center
        self.w = w  # Width of strip
        self.n = n  # Number of points (resolution)

        # Create u and v values
        self.u = np.linspace(0, 2 * np.pi, n)
        self.v = np.linspace(-w / 2, w / 2, n)
        self.U, self.V = np.meshgrid(self.u, self.v)

        # Parametric equations of Möbius strip
        self.X = (R + self.V * np.cos(self.U / 2)) * np.cos(self.U)
        self.Y = (R + self.V * np.cos(self.U / 2)) * np.sin(self.U)
        self.Z = self.V * np.sin(self.U / 2)

    def plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(self.X, self.Y, self.Z, cmap='cool', edgecolor='k', linewidth=0.2)
        ax.set_title('Mobius Strip')
        plt.show()

    def surface_area(self):
        # Estimate surface area using gradients
        dx = np.gradient(self.X)
        dy = np.gradient(self.Y)
        dz = np.gradient(self.Z)
        dA = np.sqrt(dx[0]**2 + dy[0]**2 + dz[0]**2)
        area = np.sum(dA) * (2 * np.pi / self.n) * (self.w / self.n)
        return area

    def edge_length(self):
        # Estimate edge length along one boundary
        x = self.X[0, :]
        y = self.Y[0, :]
        z = self.Z[0, :]
        length = np.sum(np.sqrt(np.diff(x)**2 + np.diff(y)**2 + np.diff(z)**2))
        return length

# Run this part
if __name__ == "__main__":
    strip = MobiusStrip(R=1, w=0.4, n=200)
    strip.plot()
    print("Estimated Surface Area:", strip.surface_area())
    print("Estimated Edge Length:", strip.edge_length())
