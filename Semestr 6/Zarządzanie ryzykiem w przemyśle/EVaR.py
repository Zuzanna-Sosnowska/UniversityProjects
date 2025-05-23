import numpy as np
import pandas as pd
from scipy.optimize import minimize
from scipy.stats import t
from arch import arch_model
from typing import Literal

# 1. Wczytanie danych
df = pd.read_csv("dane\\notowania.csv")
df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y")
df = df.sort_values("Date").set_index("Date")
df = df[df.index >= "2015-05-10"]
df = df.resample("7D").first()
prices = df["Close/Last"].str.replace("$", "").astype(float)
returns = prices.pct_change().dropna() * 100
X = returns.values

# 2. Metoda historyczna zwykła
def expectile(X, tau):
    def loss(x):
        pos = ((X - x)**2) * (X > x)
        neg = ((x - X)**2) * (X < x)
        return tau * np.mean(pos) + (1 - tau) * np.mean(neg)
    
    res = minimize(loss, x0=np.mean(X))
    return res.x[0]

# 3. Metoda parametryczna z rozkładem t-studenta
def expectile_t(tau, df, loc, scale):
    def loss(x):
        pos = ((scale**2 + (loc - x)**2) * (1 - t.cdf(x, df, loc, scale)))
        neg = ((scale**2 + (loc - x)**2) * t.cdf(x, df, loc, scale))
        return tau * pos + (1 - tau) * neg
    res = minimize(loss, x0=loc)
    return res.x[0]

# 4. Metoda historyczna (ważona)
def weighted_expectile(X, tau, lam=0.94):
    X = np.array(X)
    T = len(X)
    weights = np.array([lam**(T - t - 1) for t in range(T)])
    weights /= weights.sum()
    def loss(x):
        pos = ((X - x)**2) * (X > x)
        neg = ((x - X)**2) * (X < x)
        return tau * np.sum(weights * pos) + (1 - tau) * np.sum(weights * neg)
    res = minimize(loss, x0=np.mean(X))
    return res.x[0]

# 5. Dopasowanie rozkładu t-Studenta do danych
df_t, loc_t, scale_t = t.fit(X)

# 6. Obliczenia dla EVaR na poziomach 95% i 99%
for alpha in [0.95, 0.99]:
    print(f"\n====== EVaR dla poziomu {int(alpha*100)}% ======")

    # Parametryczna z t-Studenta
    evar_param_t = expectile_t(alpha, df_t, loc_t, scale_t)
    print(f"EVaR (parametryczna, t-Student): {evar_param_t:.4f}")

    # Monte Carlo z t-Studenta
    sim_t = t.rvs(df_t, loc=loc_t, scale=scale_t, size=10000)
    evar_mc = expectile(sim_t, alpha)
    print(f"EVaR (Monte Carlo, t-Student):   {evar_mc:.4f}")

    # Historyczna
    evar_hist = expectile(X, alpha)
    print(f"EVaR (historyczna):              {evar_hist:.4f}")

    # Historyczna ważona
    evar_hist_w = weighted_expectile(X, alpha)
    print(f"EVaR (historyczna ważona):       {evar_hist_w:.4f}")
