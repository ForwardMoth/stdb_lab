import pandas as pd
import matplotlib.pyplot as plt
import sns as sns
from scipy.stats import norm
import numpy as np
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from statsmodels.regression import linear_model

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

df_234quantile = df4[df4["count"] > first_quantile]
df6 = df_234quantile[df_234quantile["count"] < third_quantile]
# print(df6)

# 7 задание
month_count = df6['month'].value_counts()  # сразу делает по убыванию
df_month_count = pd.DataFrame({'month': month_count.index, 'month_count': month_count.values})
# print(df_month_count)

df7 = df6.merge(df_month_count, how='right', on=['month'])
# print(df7)


# 8 задание
def abs_max_scale(series):
    return series / series.abs().max()

def abs_max_scale2(series):
    return series - series.min / series.max() - series.min()

#построить 2 диаграммы по двум методам
df7['month'] = abs_max_scale(df7['month'])
df7['month_count'] = abs_max_scale(df7['month_count'])
print(df7)

list10_norm = preprocessing.normalize(df_month_count)
print(list10_norm)
df10_norm = pd.DataFrame(list10_norm, columns=['month', 'count'])
print(df10_norm)



# 9 задание
# df7['month'].plot(kind = 'bar')
#
# fig, axs = plt.subplots(1, 2)
# n_bins = len(df7)
# axs[0].hist(df7['month'], bins=n_bins)
# axs[0].set_title('month')
# axs[1].hist(df7['month_count'], bins=n_bins)
# axs[1].set_title('month_count')

# h = df7['month'].hist()
# fig = h.get_figure()
# #
# h = df7['month_count'].hist()
# fig = h.get_figure()

# x = np.arange(-3, 3, 0.001)
#
# plt.plot(x, norm.pdf(x, 0, 1))

# 10 задание
# list10_norm = preprocessing.normalize(df_month_count)
# # print(list10_norm)
# df10_norm = pd.DataFrame(list10_norm, columns=['month', 'count'])
# # print(df10_norm)
#
# x = np.array(df10_norm['month']).reshape(-1, 1)
# y = np.array(df10_norm['count'])
#
# model = LinearRegression().fit(x, y)
# R_sq = model.score(x, y)
# # The coefficients
# print("Coefficients: \n", model.coef_)
# print('Coefficient of determination:', R_sq)
#
# y_pred = model.predict(x)
# # print(y_pred)
#
# E = model.resid
# print(E)
# #регрессионные остатки
#
# # Split the data into training/testing sets
# diabetes_X_train = x[:-20]
# diabetes_X_test = x[-20:]
#
# # Split the targets into training/testing sets
# diabetes_y_train = y[:-20]
# diabetes_y_test = y[-20:]
#
# # # Plot outputs
# # plt.scatter(diabetes_X_test, diabetes_y_test, color="black")
# # plt.plot(diabetes_X_test, y_pred, color="blue", linewidth=3)
# #
# # plt.xticks(())
# # plt.yticks(())
# #
# # plt.show()
#
#
# # y_pred = model.predict(x)
# # print(y_pred)
# # plt.plot(x, y)
# # plt.plot(x, y_pred)
# # plt.show()
#

