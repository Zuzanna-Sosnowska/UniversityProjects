import numpy as np
import matplotlib.pyplot as plt

# Parametry
n_paths = 10000 # Liczba trajektori
n_steps = n_paths-1 # Liczba kroków
t_max = 100 # Czas końcowy

t = np.linspace(0, t_max, n_steps+1)
t2 = np.linspace(0, t_max, 10)
dt = t[1]-t[0]

# Proces Wienera
dW = np.sqrt(dt) * np.random.randn(n_paths, n_steps)
W = np.cumsum(dW, axis=1)
W = np.hstack((np.zeros((n_paths, 1)), W)) # Dodajemy 0 na początku W(0)=0
W = W**2
odchylenie = np.mean(W, axis = 0)

plt.title('Odchylenie')
plt.plot(t,odchylenie)
plt.scatter(t2,t2, color = 'r')
plt.show()