import pandas as pd

# Create a DataFrame with missing data represented by None
data = {'A': [1, 2, None, 4],
        'B': [5, None, 7, 8]}
df = pd.DataFrame(data)

print(df)
