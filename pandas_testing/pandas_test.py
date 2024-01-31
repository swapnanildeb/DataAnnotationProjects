import pandas as pd
import numpy as np



exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}



labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


df = pd.DataFrame(exam_data, index = labels)

print(df)

# print(df.head(3))

# print(df.tail(3))

# print(df.describe())

# print(df.iloc[[1,3,5,6],[1,3]])

# print(df[df['attempts'] > 2])


# total_rows=len(df.axes[0])
# total_cols=len(df.axes[1])

# print(df[df['score'].isnull()])

# print(df[(df['score'] >= 15) & (df['score'] <= 20)])

# print(df[(df['score'] > 15) & (df['attempts'] < 2)])

# print(df.loc['d'])
# print(df.loc[df['name'].str.contains('Anastasia')])





# df.loc[df.loc[df['name'].str.contains('Anastasia')].index, 'score'] = 11.5


# print(df.loc[df['name'].str.contains('Anastasia')])


# print(df.iloc[:, 2].sum(axis = 0))

# print(df.iloc[:, df.columns.get_loc('attempts')].sum(axis = 0))

# print(df[df['qualify'] == 'yes'])

# qualified_kids = df[df['qualify'] == 'yes'].index

# print(qualified_kids)

# print(df.loc[qualified_kids]['attempts'].sum(axis=0))

# print(df.iloc[qualified_kids, df.columns.get_loc('attempts')].sum(axis = 0))



# df.loc['d', 'score'] = 11.5

# # print(df.loc['d'])
# print(df)

# df.loc['Anastasia', 'score'] = 11.5

# print(df.loc['Anastasia'])
# print(df)

# new_row = {'name' : "Suresh", 'score': 15.5, 'attempts': 1, 'qualify': "yes"}


# df2 = pd.DataFrame([new_row], index = ['k'])
# # print(df2)

# df3 = pd.concat([df, df2])

# # df.append(new_row, ignore_index=True)
# print(df3)



# foundIndex = df3.loc[df3['name'] == 'Suresh'].index

# print(foundIndex)

# df3 = df3.drop(foundIndex)

# print(df3)



