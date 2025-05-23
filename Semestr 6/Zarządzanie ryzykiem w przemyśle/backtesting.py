import numpy as np
from typing import Literal
from scipy.stats import norm, t, chi2
from pandas import read_csv, to_datetime, Series
from arch import arch_model
from collections import Counter


def main():
    dane_notowania = read_csv('dane\\notowania.csv')
    dane_notowania['Date'] = to_datetime(dane_notowania['Date'], format='%m/%d/%Y')
    dane_notowania = dane_notowania.sort_values('Date')
    dane_notowania.set_index('Date', inplace=True)
    # Ustalenie startowej daty: 13.04.2015
    start_date = to_datetime('2015-05-10')
    dane_notowania = dane_notowania[dane_notowania.index >= start_date]
    dane_notowania = dane_notowania.resample('7D').first()
    daty_notowania = dane_notowania.index.tolist()
    dane_notowania = dane_notowania["Close/Last"].tolist()
    dane_notowania = [float(x.replace('$', '')) for x in dane_notowania]
    # aby uniknąć problemu związanemu z brakiem danych w weekendy i dni niehandlowe, bierzemy notowanie z każdego
    # poniedziałku (jeśli nie ma z danego poniedziałku, to z wtorku etc.)

    # Obliczanie tygodniowych zmian procentowych
    zmiany_procentowe = Series(dane_notowania).pct_change().dropna() * 100
    daty_zmian = daty_notowania[1:]  # pierwszy tydzień nie ma zmiany

    # Obliczanie strat
    L = -np.array(zmiany_procentowe)

    # test1 = unconditional_coverage_test(L, 0.05, 't')
    # test2 = unconditional_coverage_test(L, 0.05, 'historical')
    # test3 = unconditional_coverage_test(L, 0.05, 'weighted')
    # test4 = unconditional_coverage_test(L, 0.05, 'garch')
    # print(test1)
    # print(test2)
    # print(test3)
    # print(test4)

    christoff_test = christoffersen_test(L, 0.05, 'garch')
    print(christoff_test)


def weighted_historical_VaR(data, alpha, lambd=0.96):
    n = len(data)
    w_1 = (1 - lambd) / (1 - np.power(lambd, n))
    weights = np.power(lambd, n - np.arange(1, n + 1)) * w_1
    return np.quantile(data, alpha, weights=weights, method="inverted_cdf")


def garch_VaR(data, alpha, dist: Literal['Normal', 't'] = 'Normal'):
    # === 1. Dopasowanie modelu GARCH do zwrotów ===
    model = arch_model(data, vol='Garch', p=1, q=1, dist=dist)
    res = model.fit(disp='off')

    mu_hat = res.params['mu']
    sigma_t = res.conditional_volatility

    standardized_residuals = (data - mu_hat) / sigma_t

    q_alpha = np.quantile(standardized_residuals, alpha)

    forecast = res.forecast(horizon=1)
    sigma_n1 = np.sqrt(forecast.variance.values[-1, :])[0]

    # === 5. Oblicz VaR ===
    VaR_alpha = sigma_n1 * q_alpha + mu_hat
    return VaR_alpha


def backtesting(data, alpha, method: Literal['t', 'norm', 'historical', 'weighted', 'garch'] = 'historical'):
    I = []
    n = (len(data)) // 2
    for i in range((len(data) + 1) // 2):
        if method == 'historical':
            q = np.quantile(data[i:i + n], 1-alpha)
        elif method == 'norm':
            loc_fit, scale_fit = norm.fit(data[i:i + n])
            q = norm.ppf(1-alpha, loc=loc_fit, scale=scale_fit)
        elif method == 't':
            df_fit, loc_fit, scale_fit = t.fit(data[i:i + n])
            q = t.ppf(1-alpha, df=df_fit, loc=loc_fit, scale=scale_fit)
        elif method == 'weighted':
            q = weighted_historical_VaR(data[i:i + n], 1-alpha)
        elif method == 'garch':
            q = garch_VaR(data=data[i:i + n], alpha=1-alpha)
        else:
            raise ValueError('Niepoprawnie zadana metoda. Możliwe warianty: \'t\', \'norm\', \'historical\', \'weighted\', \'garch\'')
        if data[i+n] >= q:
            I.append(1)
        else:
            I.append(0)
    return I


def unconditional_coverage_test(data, alpha, method: Literal['t', 'norm', 'historical', 'weighted', 'garch'] = 'historical'):
    I = backtesting(data, alpha, method=method)
    i1 = np.sum(I)
    i0 = len(I) - i1

    p0 = np.mean(I)
    LR = - np.log(((1-alpha) ** i0 * alpha ** i1) / ((1 - p0) ** i0 * p0 ** i1))
    p_value = chi2.cdf(LR, df=1)
    return p_value


# TO DO:

def christoffersen_test(data, alpha, method: Literal['t', 'norm', 'historical', 'weighted', 'garch'] = 'historical'):
    I_alpha = backtesting(data, alpha, method=method)       # wektor 0 i 1 z rozkładu wielomianowego z pr sukcesu 1
    I = list(zip(I_alpha[:-1], I_alpha[1:]))
    I = Counter(I)                                          # słownik z listą wystąpień (0, 0), (0, 1), (1, 0) i (1, 1)
    pi = np.matrix([[I[(0, 0)] / (I[(0, 0)] + I[(0, 1)]), I[(0, 1)] / (I[(0, 0)] + I[(0, 1)])],
                    [I[(1, 0)] / (I[(1, 0)] + I[(1, 1)]), I[(1, 1)] / (I[(1, 0)] + I[(1, 1)])],])

    pi_est = np.mean(I_alpha)

    PI_est = np.matrix([[1 - pi_est, pi_est], [1 - pi_est, pi_est]])

    def L(pi: np.matrix):
        return ((1 - pi[0, 1]) ** I[(0, 0)] * pi[0, 1] ** I[(0, 1)] *
                (1 - pi[1, 1]) ** I[(1, 0)] * pi[1, 1] ** I[(1, 1)])

    LR = - np.log(L(PI_est) / L(pi))
    p_value = chi2.cdf(LR, df=1)
    return p_value


def berkovitz_test(data):
    pass


if __name__ == '__main__':
    main()
