import pandas as pd

# Sample data
data = {'color': ['red', 'green', 'blue', 'green', 'red']}
df = pd.DataFrame(data)

# One Hot Encoding using get_dummies()
one_hot_encoded_df = pd.get_dummies(df['color'], prefix='color')

print("One Hot Encoded DataFrame:")
print(one_hot_encoded_df)

# Label Encoding using cat.codes
df['color_label_encoded'] = df['color'].astype('category').cat.codes

print("\nLabel Encoded DataFrame:")
print(df)
