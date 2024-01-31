import pandas as pd

# df = pd.read_csv('pokemon_data.csv', delimiter=',')


print(df.head(3))
print(df.tail(3))

## Reading Headers,
print(df.columns)

## Reading specific column
# print(df['Name'][0:5])
# print(df[['Name', 'Generation', 'Legendary']][0:5])

## Reading specific row
# print(df.iloc[1])

## Reading a specific location (R, C)
# print(df.iloc[2,1])

# count = 0

# for index, row in df.iterrows():
# 	if (count == 3):
# 		break
# 	print(index)
# 	print(row['Name'])
# 	print(row['Legendary'])
# 	count += 1

# print(df.loc[df['Legendary'] == True])

# print(df.describe())

# print(df.sort_values(['HP', 'Legendary'])[['Name', 'HP', 'Legendary']])

# Index(['#', 'Name', 'Type 1', 'Type 2', 'HP', 'Attack', 'Defense', 'Sp. Atk',
#        'Sp. Def', 'Speed', 'Generation', 'Legendary'],


# df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

# df['Total'] = df.iloc[:, 4:10].sum(axis=1)

# print(df.head(3))

# print(df.sort_values(['Total'], ascending = False).head(5))

# df.to_csv('modded_poke_data.csv')

# print(df.loc[(df['Legendary'] == True) & (df['Type 1'] == 'Fire')])

new_df = df.loc[df['Name'].str.contains('Mega')]
new_df.reset_index(drop = True, inplace=True)

# print(new_df)

print(df.groupby(['Type 1']).get_group('Fire'))
