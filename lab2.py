import pandas as pd

pd.set_option('display.max_columns', 2000)
pd.set_option('display.width', 2000)

# 1 задание
df = pd.read_csv("task/globalterrorismdb_0718dist.csv", encoding='ISO-8859-1', low_memory=False)

new_df = df.loc[:, ["iyear", "imonth", "iday", "country_txt", "region_txt", "latitude", "longitude"]]





print(new_df["accident_date"])

