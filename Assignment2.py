'''Ali Nasrallah, Data Science Bootcamp Assignment 2'''

import numpy as np
import pandas as pd

#Number 1

df1 = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
filtered_df1 = df1[['Manufacturer', 'Model', 'Type']].iloc[::20]

#Number 2

df2 = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
df2.fillna(df2['Min.Price'].mean(), inplace=True)
df2.fillna(df2['Max.Price'].mean(), inplace=True)

#Number 3

df3 = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
df3_filtered = df3[np.sum(df3, axis=1)>100]

#Number 4

df4 = np.random.randint(1, 100, 16).reshape(4, 4)
df4_rows = df4.copy()
df4_columns= np.transpose(df4.copy())
adder = lambda x: np.sum(x, axis=1)
df4_row_sum = adder(df4_rows)
df4_column_sum= adder(df4_columns)

