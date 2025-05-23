from arch.__future__ import reindexing

import numpy as np
import pandas as pd
from scipy.optimize import minimize
from scipy.stats import t
from arch import arch_model
from typing import Literal
import statsmodels.api as sm

# --- 1. Wczytanie danych ---
df = pd.read_csv("dane\\notowania.csv")
df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y")
df = df.sort_values("Date").set_index("Date")
df = df[df.index >= "2015-05-10"]
df = df.resample("7D").first()
prices = df["Close/Last"].str.replace("$", "", regex=False).astype(float)
returns = prices.pct_change().dropna() * 100
X = returns.values

# --- 1. Estymacja modelu GARCH(1,1) --- 
model = arch_model(returns, vol='GARCH', p=1, q=1, mean='Constant', dist='t')
res = model.fit(disp='off')

# --- 2. Filtrowanie reszt i standaryzacja --- 
mu = res.params['mu']
sigma_t = res.conditional_volatility
eps_t = returns - mu
z_t = eps_t / sigma_t
z_t = z_t[~np.isnan(z_t)]  # usunięcie NaN
X_ = np.ones_like(z_t)

# --- 3. Expectile regression dla różnych poziomów --- 
taus = [0.01, 0.05]
evars = {}

for tau in taus:
    model_ex = sm.QuantReg(z_t, X_)  # używamy QuantileReg jako przybliżenia
    expectile = model_ex.fit(q=tau).params[0]

    # --- 4. Prognoza zmienności na kolejny okres --- 
    sigma_next = np.sqrt(res.forecast(horizon=1).variance.values[-1, 0])
    EVaR = mu + sigma_next * expectile
    evars[tau] = EVaR

# --- 5. Wyniki --- 
for tau, evar in evars.items():
    level = int((1 - tau) * 100)
    print(f"EVaR (z użyciem GARCH, t-Student): {-evar:.4f}")
    # print(f"EVaR ({level}%) = {-evar:.2f}%")
