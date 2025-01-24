import numpy as np
import pandas as pd
import derivatives as df

# Definicje funkcji i ich analitycznych pochodnych
def f1(x):
    return x**3 - 2*x

def f1_prime(x):
    return 3*x**2 - 2

def f2(x):
    return np.sin(x)

def f2_prime(x):
    return np.cos(x)

def f3(x):
    return np.exp(x)

def f3_prime(x):
    return np.exp(x)


# Obliczenia dla podanych funkcji i punktów
points = [
    {"func": f1, "prime": f1_prime, "x": 1},
    {"func": f2, "prime": f2_prime, "x": np.pi / 3},
    {"func": f3, "prime": f3_prime, "x": 0},
]

h_values = [0.1, 0.01, 0.001]
results = []

# Oblicz różnice dla każdej funkcji i punktu
for point in points:
    func, prime, x = point["func"], point["prime"], point["x"]
    exact_value = prime(x)
    for h in h_values:
        fd = df.forward_difference(func, x, h)
        cd = df.central_difference(func, x, h)
        ed = df.extrapolated_difference(func, x, h)
        results.append({
            "x": x,
            "h": h,
            "exact": exact_value,
            "forward": fd,
            "central": cd,
            "extrapolated": ed,
            "error_fd": abs(fd - exact_value),
            "error_cd": abs(cd - exact_value),
            "error_ed": abs(ed - exact_value),
        })

# Tworzenie DataFrame z wynikami
df = pd.DataFrame(results)

# Wyświetlanie tabeli w Jupyter Notebooku
df

