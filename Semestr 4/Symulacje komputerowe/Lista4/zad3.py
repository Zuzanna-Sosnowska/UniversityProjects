import matplotlib.pyplot as plt
import numpy as np


def normal_gen(n):
    # Initialize empty list to store generated samples
    xs = []
    ys = []

    # Generate samples

    for i in range(n):
        # Generate two uniform random variables in range [-1, 1]
        X = np.random.uniform(0, 1)
        Y = np.random.uniform(-1, 1)

        # Calculate squared magnitude

        if Y <= 2 * X * np.sqrt((np.log(1 / X))):
            if Y >= -2 * X * np.sqrt((np.log(1 / X))):
                xs.append(X)
                ys.append(Y)

    return xs, ys


zs = normal_gen(1000)
plt.scatter(zs[0], zs[1])

x = np.linspace(0, 1, 100)
y1 = 2 * x * np.sqrt((np.log(1 / x)))
y2 = -2 * x * np.sqrt((np.log(1 / x)))

plt.plot(x, y1)
plt.plot(x, y2)
plt.show()


plt.scatter(x, y1)
plt.show()
