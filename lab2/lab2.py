import pandas as pd
from scipy.stats import norm
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import scipy.stats as stats
import pylab as pl

pd.set_option('display.max_columns', 15)
pd.set_option('display.width', 2000)

# 1 задание
df = pd.read_csv("task/globalterrorismdb_0718dist.csv", encoding='ISO-8859-1', low_memory=False)
# print(df.head())

df.rename(columns={'iyear': 'year', 'imonth': 'month', 'iday': 'day'}, inplace=True)
# print(df.head())
#
# 2 задание
df2 = df.loc[:, ["year", "month", "day", "country_txt", "region_txt", "latitude", "longitude"]]
# print(df2)
#
df2 = df2.loc[(df2["month"] != 0) & (df2['day'] != 0)]
df2['accident_date'] = pd.to_datetime(df2.loc[:, ["year", "month", "day"]].astype(str))
# print(df2)
#
# 3 задание
columns = list(df2.columns)
new_column_order = columns[3:5] + columns[:3] + columns[-3:-1] + columns[-1:]
#
df3 = df2.reindex(columns=new_column_order)
df3.sort_values(by=new_column_order[:-1], inplace=True)
# print(df3)

ascending_order = [False, False, True, True, True, False, False]
df3.sort_values(by=new_column_order[:-1], ascending=ascending_order, inplace=True)
# print(df3)

# 4 задание
month_count = df3['country_txt'].value_counts()  # сразу делает по убыванию
df_countries_count = pd.DataFrame({'country_txt': month_count.index, 'count': month_count.values})
# print(df_countries_count)

df4 = df3.merge(df_countries_count, how='right', on=['country_txt'])
# print(df4)

# 5 задание
stat_analysis = df4.describe().reset_index()
stat_analysis.rename(columns={'index': 'parameters'}, inplace=True)
# count - кол-во непустых элементов, mean - среднее, std - среднеквадратичное отклонение
# print(stat_analysis)
# print(df4.mean(numeric_only=True))

quantile = df4.quantile(q=[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
# print(quantile)

# 6 задание
first_quantile = stat_analysis.iloc[4, 6]
# print(first_quantile)
third_quantile = stat_analysis.iloc[6, 6]
# print(third_quantile)

df6 = df4[(df4["count"] > first_quantile) & (df4["count"] < third_quantile)]
# print(df6)

# 7 задание
month_count = df6['month'].value_counts()  # сразу делает по убыванию
df_month_count1 = pd.DataFrame({'month': month_count.index, 'month_count': month_count.values})
df_month_count2 = df_month_count1.copy()
# print(df_month_count1)

df7 = df6.merge(df_month_count1, how='right', on=['month'])
# print(df7)

# 8 и 9 задание + доп задание: построить по 2 диаграммы по двум методам для month и month_count
def abs_max_scale(series):
    return series / series.abs().max()

def abs_max_scale2(series):
    return (series - series.min()) / (series.max() - series.min())

#построить 2 диаграммы по двум методам
# тут стандартизация только в month и month_count двумя способами
# Первый метод:
df_month_count1['month'] = abs_max_scale(df_month_count1['month'])
df_month_count1['month_count'] = abs_max_scale(df_month_count1['month_count'])
# print(df_month_count1)
# Второй метод:
df_month_count2['month'] = abs_max_scale2(df_month_count2['month'])
df_month_count2['month_count'] = abs_max_scale2(df_month_count2['month_count'])
# print(df_month_count2)

#ГРАФИКИ (когда 10ое делаем их закоментить) отсюда-до 10ого задания (97-152)
# это гистограмма и кривые распределения по month для ПЕРВОЙ стандартизации
df_month_count1.sort_values(by='month', inplace=True)
fit = stats.norm.pdf(df_month_count1['month'], np.mean(df_month_count1['month']), np.std(df_month_count1['month']))
# print(np.mean(df_month_count1['month']), np.std(df_month_count1['month']))
pl.plot(df_month_count1['month'], fit, label='μ: 0.5417, σ: 0.3', color='green')
pl.hist(df_month_count1['month'], edgecolor='black')
x = np.arange(0, 1, 0.01)
pl.plot(x, norm.pdf(x, 0.5417, 0.1), label='μ: 0.5417, σ: 0.1', color='red')
pl.legend(title='Parameters:')
pl.ylabel('Density')
pl.xlabel('Month')
pl.title('Normal Distributions (first method)', fontsize=14)
pl.show()

# это гистограмма и кривые распределения по month_count для ПЕРВОЙ стандартизации !
df_month_count1.sort_values(by='month_count', inplace=True)
fit = stats.norm.pdf(df_month_count1['month_count'], np.mean(df_month_count1['month_count']), np.std(df_month_count1['month_count']))
# print(np.mean(df_month_count1['month_count']), np.std(df_month_count1['month_count']))
pl.plot(df_month_count1['month_count'], fit, label='μ: 0.8903, σ: 0.07', color='green')
pl.hist(df_month_count1['month_count'], edgecolor='black')
x = np.arange(0.756844, 1, 0.0001)
pl.plot(x, norm.pdf(x, 0.8902837247523897, 0.05), label='μ: 0.8903, σ: 0.05', color='red')
pl.legend(title='Parameters:')
pl.ylabel('Density')
pl.xlabel('Month_count')
pl.title('Normal Distributions (first method)', fontsize=14)
pl.show()

# это гистограмма и кривые распределения по month для ВТОРОЙ стандартизации
df_month_count2.sort_values(by='month', inplace=True)
fit = stats.norm.pdf(df_month_count2['month'], np.mean(df_month_count2['month']), np.std(df_month_count2['month']))
# print(np.mean(df_month_count2['month']), np.std(df_month_count2['month']))
pl.plot(df_month_count2['month'], fit, label='μ: 0.5, σ: 0.3', color='green')
pl.hist(df_month_count2['month'], edgecolor='black')
x = np.arange(0, 1, 0.01)
pl.plot(x, norm.pdf(x, 0.5, 0.1), label='μ: 0.5, σ: 0.1', color='red')
pl.legend(title='Parameters:')
pl.ylabel('Density')
pl.xlabel('Month')
pl.title('Normal Distributions (second method)', fontsize=14)
pl.show()

# это гистограмма и кривые распределения по month_count для ВТОРОЙ стандартизации
df_month_count2.sort_values(by='month_count', inplace=True)
fit = stats.norm.pdf(df_month_count2['month_count'], np.mean(df_month_count2['month_count']), np.std(df_month_count2['month_count']))
# print(np.mean(df_month_count2['month_count']), np.std(df_month_count2['month_count']))
pl.plot(df_month_count2['month_count'], fit, label='μ: 0.5488, σ: 0.2886', color='green')
pl.hist(df_month_count2['month_count'], edgecolor='black')
x = np.arange(0, 1, 0.01)
pl.plot(x, norm.pdf(x, 0.5488, 0.1), label='μ: 0.5488, σ: 0.1', color='red')
pl.legend(title='Parameters:')
pl.ylabel('Density')
pl.xlabel('Month_count')
pl.title('Normal Distributions (second method)', fontsize=14)
pl.show()

# 10 задание
def linregr(df10_norm, n_of_method):
    print(df10_norm)
    x = np.array(df10_norm['month']).reshape(-1, 1)
    y = np.array(df10_norm['month_count'])

    model = LinearRegression().fit(x, y)
    R_sq = model.score(x, y)
    # The coefficients
    # print("Coefficients: \n", model.coef_)
    # print('Coefficient of determination:', R_sq)

    y_pred = model.predict(x)
    print("Y predicted = ", y_pred)
    print("Y = ", y)
    #регрессионные остатки
    Е = y - y_pred

    plt.scatter(x, y, color="black")
    plt.plot(x, y_pred, color="blue", linewidth=3)
    plt.ylabel('Month_count')
    plt.xlabel('Month')
    plt.title(f'LinearRegression ({n_of_method} method)', fontsize=14)
    plt.show()

# # Перед тем, как это запускать, закомментить графики в заданиях 8-9 (строки (97-152))
# df10_norm = df_month_count1.copy()
# linregr(df10_norm, 1)
#
# df10_norm = df_month_count2.copy()
# linregr(df10_norm, 2)