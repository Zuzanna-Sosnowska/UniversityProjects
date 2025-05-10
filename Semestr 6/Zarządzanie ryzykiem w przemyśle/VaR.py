import numpy as np
from scipy import optimize
from scipy.stats import norm, t
from pandas import read_csv, to_datetime
from typing import Literal
from arch import arch_model


def main():
    dane_notowania = read_csv('dane\\notowania.csv')
    dane_notowania['Date'] = to_datetime(dane_notowania['Date'], format='%m/%d/%Y')
    dane_notowania = dane_notowania.sort_values('Date')
    dane_notowania.set_index('Date', inplace=True)
    # Ustalenie startowej daty: 13.04.2015
    start_date = to_datetime('2015-04-13')
    dane_notowania = dane_notowania[dane_notowania.index >= start_date]
    dane_notowania = dane_notowania.resample('7D').first()
    daty_notowania = dane_notowania.index.tolist()
    dane_notowania = dane_notowania["Close/Last"].tolist()
    dane_notowania = [float(x.replace('$', '')) for x in dane_notowania]

    model = arch_model(dane_notowania, vol='Garch', p=1, q=1)
    res = model.fit(disp='off')
    print(res)

    print(maximize_likelihood_function(dane_notowania))


def likelihood_function(L, mu, c, b, s0, type: Literal['t', 'norm'] = 'norm'):
    if type == 'norm':
        return np.sum(np.log(norm.pdf(L, loc=mu, scale=sigma(L=L, c=c, b=b, s0=s0))))
    elif type == 't':
        return np.sum(np.log(t.pdf(L, mu=mu, c=c, b=b)))


def sigma(L: np.array,  c: np.array, b:np.array, s0: np.array):
    list_of_sigmas = []
    for i in range(len(L)):
        list_of_sigmas.append(sigma_i(L, b, c, i, s0))
    return list_of_sigmas


def sigma_i(L, b, c, i, s0):
    return c[0] + np.sum(c[1:] * np.power(L[i - 2::-1], 2)) + np.sum(b * np.power(s0[i - 2::-1], 2))


def maximize_likelihood_function(L, type: Literal['t', 'norm'] = 'norm'):
    return optimize.minimize(lambda x: likelihood_function(L, c = x[0], b = x[1], s0 = x[2], mu = x[3], type=type),
                             [np.ones(1), np.ones(1), np.ones(1), 0])


if __name__ == '__main__':
    main()
