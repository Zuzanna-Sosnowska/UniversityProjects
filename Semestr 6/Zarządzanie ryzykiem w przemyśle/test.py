import numpy as np
import pandas as pd
from arch import arch_model
from pandas import read_csv, to_datetime

# def select_garch_order(returns, max_p=5, max_q=5, criterion='aic'):
#     best_score = np.inf
#     best_order = None
#     results = []
#
#     for p in range(max_p + 1):
#         for q in range(max_q + 1):
#             if p == 0 and q == 0:
#                 continue  # GARCH(0,0) nie ma sensu
#             try:
#                 model = arch_model(returns, vol='Garch', p=p, q=q, dist='normal')
#                 res = model.fit(disp='off')
#                 score = res.aic if criterion == 'aic' else res.bic
#                 results.append({'p': p, 'q': q, criterion: score})
#                 if score < best_score:
#                     best_score = score
#                     best_order = (p, q)
#             except Exception as e:
#                 print(f'Błąd dla p={p}, q={q}: {e}')
#                 continue
#
#     results_df = pd.DataFrame(results)
#     return best_order, results_df.sort_values(by=criterion)
#
# dane_notowania = read_csv('dane\\notowania.csv')
# dane_notowania['Date'] = to_datetime(dane_notowania['Date'], format='%m/%d/%Y')
# dane_notowania = dane_notowania.sort_values('Date')
# dane_notowania.set_index('Date', inplace=True)
# start_date = to_datetime('2015-04-13')
# dane_notowania = dane_notowania[dane_notowania.index >= start_date]
# dane_notowania = dane_notowania.resample('7D').first()
# daty_notowania = dane_notowania.index.tolist()
# dane_notowania = dane_notowania["Close/Last"].tolist()
# dane_notowania = [float(x.replace('$', '')) for x in dane_notowania]
#
# # 🔍 Szukaj najlepszego modelu GARCH
# najlepszy_model, tabela = select_garch_order(dane_notowania, max_p=5, max_q=5, criterion='aic')
#
# print(f"✅ Najlepszy model GARCH(p,q): p={najlepszy_model[0]}, q={najlepszy_model[1]}")
# print("\n📊 Tabela wyników:")
# print(tabela.head(10))  # pokazuje top 10 modeli
