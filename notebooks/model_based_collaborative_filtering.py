
# Model-based collaborative filtering system

# 1. Recommend items to users based on purchase history and similarity of ratings provided by other users      who bought items to that of a particular customer.
# 2. A model based collaborative filtering technique is chosen here as it helps in predicting products for      a particular user by identifying patterns based on preferences from multiple user data.


# import the libraries

import numpy as np 
import pandas as pd 
import sklearn
from sklearn.decomposition import TruncatedSVD
import matplotlib.pyplot as plt


# load the data
df = pd.read_csv('ratings_Beauty.csv')


# top 10k records(subset) from the original dataset
df1 = df.head(10000)

# Utility Matrix based on products sold and user reviews

# Utility Matrix : An utlity matrix is consists of all possible user-item preferences (ratings) details     represented as a matrix. The utility matrix is sparce as none of the users would buy all the items in     the list, hence, most of the values are unknown.

df1_utility_matrix = df1.pivot_table(values='Rating', index='UserId', columns='ProductId', fill_value=0)

# transpose of the utility matrix
X = df1_utility_matrix.T



# Decomposing the matrix
svd = TruncatedSVD(n_components=10)
decomposed_matrix = svd.fit_transform(X)


# correlation matrix
correlation_matrix = np.corrcoef(decomposed_matrix)

# isolating product id #6117036094 from the correlational matrix
i = '6117036094'
product_name = list(X.index)
product_id = product_name.index(i)


# Recommending top 10 highly correlated products in sequence

recommend = list(X.index[correlation_product_id>0.90])

# remove the product already brought by the customer
recommend.remove(i)

recommend[0:9]
