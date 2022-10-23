import pandas as pd

pd.set_option('display.max_columns', 15)
pd.set_option('display.width', 2000)

# 1 задание
df = pd.read_csv("task/globalterrorismdb_0718dist.csv", encoding='ISO-8859-1', low_memory=False)

# print(df.head())

df.rename(columns={'iyear': 'year', 'imonth': 'month', 'iday': 'day'}, inplace=True)

# 2 задание
new_df = df.loc[:, ["year", "month", "day", "country_txt", "region_txt", "latitude", "longitude"]]

new_df = new_df.loc[(new_df["month"] != 0) & (new_df['day'] != 0)]

new_df['accident_date'] = pd.to_datetime(new_df.loc[:, ["year", "month", "day"]].astype(str))

# print(new_df)

# 3 задание

columns = list(new_df.columns)

new_column_order = columns[3:5] + columns[:3] + columns[-3:-1] + columns[-1:]

new_df = new_df.reindex(columns=new_column_order)

new_df.sort_values(by=new_column_order[:-1], inplace=True)

# ascending_order = [False, False, True, True, True, False, False]
# new_df.sort_values(by=new_column_order[:-1], ascending=ascending_order, inplace=True)

# print(new_df)

# 4 задание

countries_count = new_df['country_txt'].value_counts()

df_countries_count = pd.DataFrame({'country_txt': countries_count.index, 'count': countries_count.values})

print(df_countries_count)

# df4 = pd.merge(new_df, df_countries_count)
# print(df4)

