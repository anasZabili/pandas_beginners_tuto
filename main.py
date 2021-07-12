import pandas as pd
import re

# Loading data from file
pokeData = pd.read_csv('pokemon_data.csv')
pokeDataFromTxt = pd.read_csv('pokemon_data.txt', delimiter='\t')
print(pokeData)


# Print the top the data
print(pokeData.head(3))


# Print tail of the data
print(pokeData.tail(3))


# Read the header of the file
print(pokeData.columns)


# Print a column
print(pokeData['Name'][0 : 10])
# or pokeDate.Name


# Print multiple columns
print(pokeData[['Name', 'HP']][0 : 10])


#Print each row from integer position
print(pokeData.iloc[1 : 4])


# Print a specific location from integer position(Row, Column)
print(pokeData.iloc[2, 1])


#Print a specific location from condition on Label
print(pokeData.loc[pokeData['Type 1'] == "Fire"])


# Iterate through each row
# for index, row in pokeData.iterrows():
#   print(index, row['Name'])


# Describing data (stats of the data)
print(pokeData.describe())


# Sort data by column value
print(pokeData.sort_values('Name'))
# print(pokeData.sort_values('Name', ascending=False))


# Sort data by multiple columns value
print(pokeData.sort_values(['HP', 'Name']))


# Adding a new column
# pokeData['Total'] = (pokeData['HP'] + pokeData['Attack'] + pokeData['Defense'] 
#   + pokeData['Sp. Atk'] + pokeData['Sp. Def'] + pokeData['Speed'])
# Or (more efficient)
pokeData['Total'] = pokeData.iloc[:, 4:10].sum(axis=1)
# print(pokeData)


# Moving a column
cols = list(pokeData.columns.values) # return a list who contain all the columns header 
pokeData = pokeData[cols[0: 4] + [cols[-1]]+cols[4:12]]
print(pokeData)


# Drop a column
deletedData = pokeData.drop(columns=['Total'])
# print(deletedData)


# Saving the new CSV
pokeData.to_csv('modifiedPokemon.csv', index=False) # pass the index = False to not save the index in the file


# Saving to txt
pokeData.to_csv('modifiedPokemon.txt', index=False, sep='\t')


# Filtering data (in pandas and numpy and = &, or = |, not = ~)
# print(pokeData.loc[(pokeData['Type 1'] == 'Grass') | (pokeData['Type 2'] == 'Poison')])
new_df = pokeData.loc[(pokeData['Type 1'] == 'Grass') & (pokeData['Type 2'] == 'Poison') & (pokeData['HP'] > 70)]
# reset the index so the new data don't have the old none filtered index
new_df = new_df.reset_index(drop=True) # by default the old index gonna be stored 
# in a column to avoid that we can specify drop=True 
new_df.to_csv('filtered.csv', index=False) 
print(new_df)


#Filter by name following a pattern
print(pokeData.loc[~pokeData['Name'].str.contains('Mega')])


# Filter by regex
print(pokeData.loc[pokeData['Type 1'].str.contains('fire|grass', flags=re.IGNORECASE, regex = True)])
print(pokeData.loc[pokeData['Name'].str.contains('^pi[a-z]*', flags=re.IGNORECASE, regex = True)])


# Conditional Changes
pokeData.loc[pokeData['Type 1'] == 'Fire', 'Type 1'] = 'Flamer' 
# print(pokeData.loc[pokeData['Type 1'].str.contains('Flamer')])
pokeData.loc[pokeData['Total'] > 500, ['Generation', 'Legendary']] = ['infinite', True]
# Here we do a multiple change is the total is > 500, Generation and Legendary equal Strong
print(pokeData)
# reset the data
pokeData = pd.read_csv("modifiedPokemon.csv")


# Group BY + min + sum + count
print(pokeData.groupby(['Type 1']).mean().sort_values('HP', ascending=False).iloc[:, :5])
print(pokeData.groupby(['Type 1']).sum().sort_values('HP', ascending=False).iloc[:, :5])
# To do a clean count a good practice is to set a count column equal to 1 before de the groupby
pokeData['count'] = 1
print(pokeData.groupby(['Type 1', 'Type 2']).count()['count'])


# Large data set Chunks
for df in pd.read_csv("modifiedPokemon.csv", chunksize=5):
  print("chunk")
  print(df) # this df only contain 5 rows at each iteration

# Chunk size is the number of line loded at the time in the memorie