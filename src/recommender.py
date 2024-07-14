
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class Recommender:
    def __init__(self, df):
        self.df = df
        self.similarity_matrix = None
    
    def set_similarity_matrix(self, features):
        """Build and set similarity matrix

        Args:
            features: np array of stacked features
        """
        self.similarity_matrix = cosine_similarity(features, features)
    
    def recommend(self, title: str, top_n: int = 20):
        """Generates a recommendation based off the similarity matrix and the title's synopsis

        Args:
            title (str): Title of Manga in MyAnimeList
            top_n (int, optional): Number of recommendations. Defaults to 20.

        Returns:
            list[str]: list of reommendations
        """
        idx = self.df[self.df['title'] == title].index[0]
        sim_scores = list(enumerate(self.similarity_matrix[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_indices = [i[0] for i in sim_scores[1:top_n+1]]
        
        to_list = self.df['title'].iloc[sim_indices].tolist()
        return to_list