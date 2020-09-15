'''
@author : jhhalls
'''

from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

class SimilarityPredictions(object):
    '''This class calculates a similarity matrix from latent embeddings.
    Input: embeddings - a pandas dataframe of items and latent dimensions.
    '''

    def __init__(self, embeddings):
        self.embeddings = embeddings
        self.ids = embeddings.index.tolist()

    def calculate_cosine_similarity_matrix(self):
        '''Calculates a cosine similarity matrix from the embeddings'''
        similarity_matrix = pd.DataFrame(cosine_similarity(
            X=self.embeddings),
            index=self.ids)
        similarity_matrix.columns = self.ids
        return similarity_matrix

    def predict_similar_items(self, seed_item, n):
        '''Use the similarity_matrix to return n most similar items.'''
        similar_items = pd.DataFrame(self.similarity_matrix.loc[seed_item])
        similar_items.columns = ["similarity_score"]
        similar_items = similar_items.sort_values('similarity_score', ascending=False)
        similar_items = similar_items.head(n)
        similar_items.reset_index(inplace=True)
        similar_items = similar_items.rename(index=str, columns={"index": "item_id"})
        return similar_items.to_dict()
