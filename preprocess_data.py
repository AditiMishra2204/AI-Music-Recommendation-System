import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import os

# Read the dataset
df = pd.read_csv(r"C:\Users\ADITI MISHRA\Desktop\music file 2\MRS\MRS\data\ex.csv")

# Perform data preprocessing
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
df['User-Rating'] = df['User-Rating'].apply(lambda x: x[0:3])
df['Album/Movie'] = df['Album/Movie'].str.replace(' ', '')
df['Singer/Artists'] = df['Singer/Artists'].str.split(', ')  # Split combined artist names into a list
df['tags'] = df.apply(lambda row: ' '.join(row['Singer/Artists']) + ' ' + row['Genre'] + ' ' + row['Album/Movie'] + ' ' + row['User-Rating'], axis=1)

# Create feature vectors
cv = CountVectorizer(max_features=2000)
vectors = cv.fit_transform(df['tags']).toarray()

# Calculate similarity matrix
similarity = cosine_similarity(vectors)

# Create a copy of the DataFrame
new_df = df[['Song-Name', 'tags']].copy()

# Rename columns in the copied DataFrame
new_df.rename(columns={'Song-Name': 'title'}, inplace=True)


# Define recommendation function
def recommend(music):
    music_index = new_df[new_df['title'] == music].index[0]
    distances = similarity[music_index]
    music_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    for i in music_list:
        print(new_df.iloc[i[0]].title)

# Save trained model
os.makedirs('models', exist_ok=True)
pickle.dump(new_df, open('models/musicrec.pkl', 'wb'))
pickle.dump(similarity, open('models/similarities.pkl', 'wb'))
