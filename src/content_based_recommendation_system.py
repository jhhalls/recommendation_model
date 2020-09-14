'''
@author : jhhalls
'''

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

###### helper functions. Use them when needed #######
def get_title_from_index(index):
	return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
	return df[df.title == title]["index"].values[0]

##################################################


##Step 1: Read CSV File
movies_dataset = pd.read_csv('movie_dataset.csv')

##Step 2: Select Features
features  = ['keywords', 'cast', 'genres', 'director']

# fill the null value with empty space
for feature in features:
    movies_dataset[feature] = movies_dataset[feature].fillna('')


##Step 3: Create a column in DataFrame which combines all selected features
def combine_feature(row):
#     try opertation
    try:
        return row['keywords']+' '+ row['cast']+' '+row['director']+' '+row['genres']
#     
    except:
        print('Error',row)


        
movies_dataset['combine_features'] = movies_dataset.apply(combine_feature, axis=1)
        
       
##Step 4: Create count matrix from this new combined column

cv = CountVectorizer()
count_matrix = cv.fit_transform(movies_dataset['combine_features'])


##Step 5: Compute the Cosine Similarity based on the count_matrix
cosine_similarity = cosine_similarity(count_matrix)

movie_user_likes = "Avatar"

## Step 6: Get index of this movie from its title
###### helper functions. Use them when needed #######
def get_title_from_index(index):
    try:
        return movies_dataset[movies_dataset.index == index]["title"].values[0]
    except:
        return "error", index
    
    
    
def get_index_from_title(title):
	return movies_dataset[movies_dataset.title == title]["index"].values[0]


movie_index = get_index_from_title(movie_user_likes)
similar_movies = list(enumerate(cosine_similarity[movie_index]))


## Step 7: Get a list of similar movies in descending order of similarity score
sorted_similar_movies = sorted(similar_movies, key= lambda x:x[1], reverse=True)

## Step 8: Print titles of first 50 movies

i=0
for movie in sorted_similar_movies:
    print (get_title_from_index(movie[0]))
    i=i+1
    if i>50:
        break
