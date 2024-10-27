import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

polski2015 = pd.read_csv('polski2015.csv')
polski2023 = pd.read_csv('polski2023.csv')

#dane 2015
sredni_wynik2015 = polski2015['średni wynik (%)']
uczniowie2015 = polski2015['* liczba zdających']
RSPO_2015 = polski2015['RSPO szkoły']
zdawalnosc_2015 = polski2015['* zdawalność (%).1']

#dane 2023
sredni_wynik2023 = polski2023['średni wynik (%)']
uczniowie2023 = polski2023['* liczba zdających']
RSPO_2023 = polski2023['RSPO szkoły']
zdawalnosc_2023 = polski2023['* zdawalność (%).1']

plt.figure(figsize=(16, 6))

#2015
plt.subplot(1,2,1)
plt.title('Formuła 2015')
plt.hist(sredni_wynik2015, bins=50, density=True, alpha=0.6)
sns.kdeplot(sredni_wynik2015, label='Gęstość empiryczna')
plt.axvline(np.mean(sredni_wynik2015), color='red', linestyle='--', label='Wartość oczekiwana')
plt.axvline(np.median(sredni_wynik2015), color='green', linestyle='--', label='Mediana')
plt.legend()

#2023
plt.subplot(1,2,2)
plt.title('Formuła 2023')
plt.hist(sredni_wynik2023, bins=50, density=True, alpha=0.6)
sns.kdeplot(sredni_wynik2023, label='Gęstość empiryczna')
plt.axvline(np.mean(sredni_wynik2023), color='red', linestyle='--', label='Wartość oczekiwana')
plt.axvline(np.median(sredni_wynik2023), color='green', linestyle='--', label='Mediana')
plt.legend()

plt.savefig('obrazki\gestosc.png')
plt.show()