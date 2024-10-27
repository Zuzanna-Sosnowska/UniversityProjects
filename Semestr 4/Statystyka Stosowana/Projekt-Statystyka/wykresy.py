import funkcje as f
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np


a = pd.read_csv('polski2015.csv')
b = pd.read_csv('polski2023.csv')

x_1 = a['* liczba zdających']
y_1 = a['* zdawalność (%).1']
z_1 = a['średni wynik (%)']

x_2 = b['* liczba zdających']
y_2 = b['* zdawalność (%).1']
z_2 = b['średni wynik (%)']


""" Histogramy reprezentujące gęstość empiryczną """

# sns.kdeplot(z_1, color='navy')
# sns.kdeplot(z_2, color='red')
# plt.legend(['formuła 2015', 'formuła 2023'], loc='best')
# plt.title("Średni wynik egzaminu maturalnego z j. polskiego")
# plt.show()

""" Wykres reprezentujący dystrybuantę empiryczną """
#
# sns.ecdfplot(z_1, color='navy')
# sns.ecdfplot(z_2, color='red')
# plt.legend(['formuła 2015', 'formuła 2023'], loc='best')
# plt.title("Wykres reprezentujący dystrybuantę")
# plt.show()

""" Boxplot """
#
# plt.boxplot(z_1)
# plt.title('Boxplot - formuła 2015')
# plt.show()
#
# plt.boxplot(z_2)
# plt.title('Boxplot - formuła 2023')
# plt.show()

""" Wykresy przedstawiające wartość średniej ucinanej/windsorowskiej w zależności od ilości uciętych wartości"""

x_list = [k for k in range(len(z_1)//2 - 1)]
y1_list = [f.cut_mean(z_1, k) for k in range(len(z_1)//2 - 1)]
y2_list = [f.windsor_mean(z_1, k) for k in range(len(z_1)//2 - 1)]

plt.figure(figsize=(7, 6))

plt.subplot(2, 1, 1)
plt.plot(x_list, y1_list)
plt.axhline(y=f.arithmetic_mean(z_1), color='r', linestyle='-')
plt.axhline(y=f.median(z_1), color='g', linestyle='-')
plt.title('Średnia ucinana - formuła 2015', fontsize=13)

plt.subplot(2, 1, 2)
plt.plot(x_list, y2_list)
plt.axhline(y=f.arithmetic_mean(z_1), color='r', linestyle='-')
plt.axhline(y=f.median(z_1), color='g', linestyle='-')

plt.subplots_adjust(hspace=0.5)
plt.title('Średnia windsorowska - formuła 2015', fontsize=13)
plt.show()


y3_list = [f.cut_mean(z_2, k) for k in range(len(z_1)//2 - 1)]
y4_list = [f.windsor_mean(z_2, k) for k in range(len(z_1)//2 - 1)]

plt.figure(figsize=(7, 6))

plt.subplot(2, 1, 1)
plt.plot(x_list, y3_list)
plt.axhline(y=f.arithmetic_mean(z_2), color='r', linestyle='-')
plt.axhline(y=f.median(z_2), color='g', linestyle='-')
plt.title('Średnia ucinana - formuła 2023', fontsize=13)

plt.subplot(2, 1, 2)
plt.plot(x_list, y4_list)
plt.axhline(y=f.arithmetic_mean(z_2), color='r', linestyle='-')
plt.axhline(y=f.median(z_2), color='g', linestyle='-')

plt.subplots_adjust(hspace=0.5)
plt.title('Średnia windsorowska - formuła 2023', fontsize=13)
plt.show()
