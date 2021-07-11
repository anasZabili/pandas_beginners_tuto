import pandas as pd

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