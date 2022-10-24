import pandas as pd

pd.set_option('display.max_columns', 15)
pd.set_option('display.width', 2000)

# 1 задание
df = pd.read_csv("task/globalterrorismdb_0718dist.csv", encoding='ISO-8859-1', low_memory=False)
# print(df.head())

df.rename(columns={'iyear': 'year', 'imonth': 'month', 'iday': 'day'}, inplace=True)
# print(df.head())

# 2 задание
df2 = df.loc[:, ["year", "month", "day", "country_txt", "region_txt", "latitude", "longitude"]]
#print(df2)

df2 = df2.loc[(df2["month"] != 0) & (df2['day'] != 0)]
df2['accident_date'] = pd.to_datetime(df2.loc[:, ["year", "month", "day"]].astype(str))
#print(df2)

# 3 задание
columns = list(df2.columns)
new_column_order = columns[3:5] + columns[:3] + columns[-3:-1] + columns[-1:]

df3 = df2.reindex(columns=new_column_order)
df3.sort_values(by=new_column_order[:-1], inplace=True)
# print(df3)

# ascending_order = [False, False, True, True, True, False, False]
# df3.sort_values(by=new_column_order[:-1], ascending=ascending_order, inplace=True)
# print(df3)

# 4 задание
countries_count = df3['country_txt'].value_counts()

df_countries_count = pd.DataFrame({'country_txt': countries_count.index, 'count': countries_count.values})
print(df_countries_count)

# df4 = pd.merge(df3, df_countries_count)
# print(df4)

# 5 задание