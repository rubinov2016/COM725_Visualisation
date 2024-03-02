import pandas as pd
df = pd.read_csv("null_values_dataset.csv")

df_gears_null = pd.isnull(df["Number of gears"])
print("Number of NULL gears = ", df_gears_null.sum())

df_nulls = df.isnull()
null_count = df_nulls.sum().sum()
print("Number of NULL in the whole dataset = ",null_count)
rows_with_nulls = (df.isnull().sum(axis=1) >= 1).sum()
print("Number of NULL rows = ", rows_with_nulls)
rows_with_nulls = (df.isnull().sum() >= 1).sum()
print("Number 2 of NULL rows = ", rows_with_nulls)
rows_with_nulls = (df.isnull().sum(axis=0) >= 1).sum()
print("Number 3 of NULL rows = ", rows_with_nulls)

null_values_row_22 = df.iloc[21].isnull().sum()
print("Number of null values in row 22:", null_values_row_22)
null_values_in_range = df.iloc[23:40].isnull().sum().sum()
print("Number of null values from row 24 to row 40:")
print(null_values_in_range)
