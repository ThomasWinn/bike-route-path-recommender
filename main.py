import numpy as np
import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer

from src.embeddings import Embeddings
from src.recommender import Recommender

TITLE='Gantz'
MODEL = 'paraphrase-mpnet-base-v2'

def main():
    
    # Load in DF
    df = pd.read_csv('data/processed/manga_cleaned_' + MODEL + '.csv')
    
    recommender = Recommender(df=df)
    embeddings = Embeddings(model_name=MODEL, df=df)
    
    synopsis_embeddings = embeddings.load('data/embeddings/synopsis_embeddings.npz')
    
    mlb = MultiLabelBinarizer()

    # one hot encode the themes, genres, and demographics
    genres_encoded = mlb.fit_transform(df['genres'])
    themes_encoded = mlb.fit_transform(df['themes'])
    demographics_encoded = mlb.fit_transform(df['demographics'])
    
    # Combine all features into a single DataFrame
    combined_features = np.hstack([
        synopsis_embeddings, # 768
        genres_encoded, # 39
        themes_encoded, # 50
        demographics_encoded # 17
    ])
    
    recommender.set_similarity_matrix(combined_features)
    
    print(recommender.recommend(title=TITLE))

if __name__ == "__main__":
    main()