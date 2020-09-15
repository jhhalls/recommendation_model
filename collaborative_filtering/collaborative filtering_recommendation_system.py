import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


###### helper functions. Use them when needed #######
## helper Function
def get_similar_movies(movie_name, user_rating):
    similar_score = item_similarity_df[movie_name]*(user_rating - 2.5)
    similar_score = similar_score.sort_values(ascending=False)
    
    return similar_score

##################################################

## Read CSV File
ratings = pd.read_csv('ratings.csv')
movies = pd.read_csv('movies.csv')


## Merge the two datasets and drop unnecessary features 
ratings = pd.merge(movies, ratings).drop(['genres', 'timestamp'], axis=1)


## Create a pivot table of movies and  user rating
user_rating = ratings.pivot_table(index=['userId'], columns=['title'], values = 'rating')


## Drop all the columns where less than 10 users have rated them
user_rating = user_rating.dropna(thresh=10, axis=1).fillna(0)


## lets build a similarity matrix
item_similarity_df = user_rating.corr(method='pearson')



# list of tuples of movies with their ratings
action = [ ('eXistenZ (1999)', 4), ('10 Things I Hate About You (1999)', 4.5), ('12 Years a Slave (2013)', 5)]


## Similar Movies dataframe
similar_movies = pd.DataFrame()

for movie,rating in action:
    
    similar_movies = similar_movies.append(get_similar_movies(movie,rating), ignore_index = True)

    
recommended_movies = pd.DataFrame(similar_movies.sum().sort_values(ascending = False))



## Step 7: Get a list of similar movies in descending order of similarity score
recommended_movies_list = list(recommended_movies.T.columns)

## Step 8: Print titles of first 50 movies
print(recommended_movies_list)