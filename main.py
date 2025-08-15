# importing lib.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
df = pd.read_csv('mymoviedb.csv', lineterminator='\n')
head = df.head()
# print(head)
# viewing dataset info
info = df.info()
# print(info)
# exploring genres column
head_genre =df['Genre'].head()
# print(head_genre)
# check for duplicated rows
check_duplicated =df.duplicated().sum()
# print(check_duplicated)
# exploring summary statistics
statistics =df.describe()
# print(statistics)

# -----------------------------------------------------------------------------------
# Exploration Summary
# we have a dataframe consisting of 9827 rows and 9 columns.
# our dataset looks a bit tidy with no NaNs nor duplicated values.
# Release_Date column needs to be casted into date time.
# Overview, Original_Languege and Poster-Url wouldn't be so useful during analys.
# there is noticable outliers in Popularity column
# Vote_Average bettter be categorised for proper analysis.
# Data Cleaning
# Genre column has comma saperated values and white spaces
#--------------------------------------------------------------------------------------------


# casting column a
df['Release_Date'] = pd.to_datetime(df['Release_Date'])
# confirming changes
#print(df['Release_Date'].dtypes)
df['Release_Date'] = df['Release_Date'].dt.year
df['Release_Date'].dtypes

#print(df.info())


# making list of column to be dropped
cols = ['Overview', 'Original_Language', 'Poster_Url']

#dropping columns and confirming changes
df.drop(cols, axis = 1, inplace = True)
# print(df.columns())


def catigorize_col (df, col, labels):
    """
    catigorizes a certain column based on its quartiles
   
    Args:
        (df)     df   - dataframe we are proccesing
        (col)    str  - to be catigorized column's name 
        (labels) list - list of labels from min to max
    
    Returns:
        (df)     df   - dataframe with the categorized col
    """
    
    # setting the edges to cut the column accordingly
    edges = [df[col].describe()['min'],
             df[col].describe()['25%'],
             df[col].describe()['50%'],
             df[col].describe()['75%'],
             df[col].describe()['max']]
    df[col] = pd.cut(df[col], edges, labels = labels, duplicates='drop')
    return df

# define labels for edges
labels = ['not_popular', 'below_avg', 'average', 'popular']
# categorize column based on labels and edges
catigorize_col(df, 'Vote_Average', labels)
# confirming changes
df['Vote_Average'].unique()


# exploring column
# print(df['Vote_Average'].value_counts())


# dropping NaNs
df.dropna(inplace = True)
# confirming
df.isna().sum()

# split the strings into lists
df['Genre'] = df['Genre'].str.split(', ')
# explode the lists
df = df.explode('Genre').reset_index(drop=True)
df.head()


# casting column into category
df['Genre'] = df['Genre'].astype('category')
# confirming changes
df['Genre'].dtypes


df.nunique()


# setting up seaborn configurations
sns.set_style('whitegrid') 

# showing stats. on genre column
df['Genre'].describe()

# visualizing genre column
sns.catplot(y = 'Genre', data = df, kind = 'count', 
order = df['Genre'].value_counts().index,
color = '#4287f5')
plt.title('genre column distribution')
plt.show()



# visualizing vote_average column
sns.catplot(y = 'Vote_Average', data = df, kind = 'count', 
order = df['Vote_Average'].value_counts().index,
color = '#4287f5')
plt.title('votes destribution')
plt.show()




# checking max popularity in dataset
print(df[df['Popularity'] == df['Popularity'].max()])



# checking max popularity in dataset
print(df[df['Popularity'] == df['Popularity'].min()])


df['Release_Date'].hist()
plt.title('Release_Date column distribution')
plt.show()