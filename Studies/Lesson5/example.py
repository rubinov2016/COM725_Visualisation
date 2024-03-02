import pandas as pd

# Example DataFrame with missing values
data = {'A': [1, 2, None, 4],
        'B': [5, None, 7, 8],
        'C': [None, None, None, None]}
df = pd.DataFrame(data)
df.info()
df.describe()

# Drop rows with any missing values
df_cleaned = df.dropna(axis=0, how='any')

print(df_cleaned)

# dict_of_lists = {"age": [32, 43],"name": ["Hill","Onio"]}
# new_df = pd.DataFrame(dict_of_lists)
# print(new_df)

mydict = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
          {'a': 100, 'b': 200, 'c': 300, 'd': 400},
          {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000}]
df = pd.DataFrame(mydict)
print(df)
print("df.iloc[0] \n", df.iloc[0])
print("df.iloc[[0]] \n", df.iloc[[0]])
print("df.iloc[[0, 1]]: \n", df.iloc[[0, 1]])
print(df.iloc[lambda x: x.index % 2 == 1])
print("df.iloc[0, 1]: \n", df.iloc[0, 1])