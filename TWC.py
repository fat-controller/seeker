#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as ny


# In[ ]:


print("SEARCHER")

# Read in data from the keywords / config file
df_search = pd.read_csv('keywords.csv')

print("Loaded config file")


# Make data lowercase
for i in range(2):
    col_name = df_search.columns[i]
    df_search[col_name] = df_search[col_name].str.lower()

print("Search words made lower case")

# Create lists from the data
keywords_hard = df_search.iloc[:,0].tolist()
keywords_soft = df_search.iloc[:,1].tolist()
search_columns = df_search.iloc[:,2].tolist()

print("Search words moved to lists")

# Strip out blanks
keywords_hard = [item for item in keywords_hard if not pd.isna(item)]
keywords_soft = [item for item in keywords_soft if not pd.isna(item)]
search_columns = [item for item in search_columns if not pd.isna(item)]

print("Blank search words removed")


# In[ ]:


print("Details for debugging...")
print(str(len(keywords_hard))+ " Hard search words:")
print(keywords_hard)
print("")
print(str(len(keywords_soft))+ " Soft search words:")
print(keywords_soft)
print("")
print(str(len(search_columns))+ " Columns to search:")
print(search_columns)
print("")
print("!! Set up complete")
print("")


# In[ ]:


# load the CSV file
df_data = pd.read_csv('DATA.csv')

print("Loaded search file")

# Create columns that will be used to flag matched records
df_data['MATCH-HARD'] = False
df_data['MATCH-SOFT'] = False
df_data['MATCH'] = False
print("Created flag fields and set to False")


# In[ ]:


# Hard matches first
# Iterate through each key word, searching each of the columns
# If a value matches then change the MATCH field to TRUE

for keyword in keywords_hard:
    for col in search_columns:
        df_data['MATCH-HARD'] = df_data['MATCH-HARD'] | df_data[col].astype(str).str.contains(keyword, case=False, na=False)

print("Hard search complete")

for keyword in keywords_soft:
    for col in search_columns:
        df_data['MATCH-SOFT'] = df_data['MATCH-SOFT'] | df_data[col].astype(str).str.contains(keyword, case=False, na=False)

df_data['MATCH'] = df_data['MATCH-HARD'] | df_data['MATCH-SOFT']

print("Soft search complete")


# In[ ]:


# Export data to a new CSV
df_data.to_csv('Data-Processed.csv', index=False)
print("Processed data saved to new CSV file")
print("")
print("!!SEARCHER COMPLETE")


# In[ ]:




