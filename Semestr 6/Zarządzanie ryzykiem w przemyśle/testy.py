import numpy as np
from pandas import read_csv, to_datetime, Series
from typing import Literal
from arch import arch_model
from scipy import optimize
from scipy.stats import norm, t


def likelihood_function(L, mu, c0, c, b, s0, type: Literal['t', 'norm'] = 'norm'):
    if type == 'norm':
        scale = sigma(L, c0, c, b, s0)
        pdf = norm.pdf(L, loc=mu, scale=scale)
        return np.sum(np.log(pdf, out=pdf, where=pdf>0))
    elif type == 't':
        df_fit, loc_fit, scale_fit = t.fit(L)
        return np.sum(np.log(t.pdf(L, df=df_fit, loc=mu, scale=sigma(L, c0, c, b, s0))))


def sigma(L, c0, c1, b1, s0):
    sigma_list = [s0 ** 2]
    for i in range(1, len(L)):
        sigma_list.append(c0 + c1 * np.power(L[i-1], 2) + b1 * sigma_list[i - 1])
    return np.sqrt(sigma_list)


def maximize_likelihood_function(L, type: Literal['t', 'norm'] = 'norm'):
    return optimize.minimize(lambda x: -likelihood_function(L, c0 = x[0], c = x[1], b = x[2], s0 = x[3], mu = x[4], type=type),
                             np.array([2.37, 0, 0, 2.37, 0]))


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
    # Obliczanie tygodniowych zmian procentowych
    zmiany_procentowe = Series(dane_notowania).pct_change().dropna() * 100

    # Unormowane dane lub oryginalne zmiany procentowe:
    data = np.array(zmiany_procentowe)

    # print(maximize_likelihood_function(data))

    # Dopasuj model GARCH(1, 1)
    model = arch_model(data, vol='Garch', p=2, q=2)
    res = model.fit(disp="off")
    print(res)


if __name__ == '__main__':
    main()

