import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer

class Embeddings:
    def __init__(self, model_name, dataframe):
        self.model_name = model_name
        self.df = dataframe

    def encode(self):
        # Assuming the column containing synopses is named 'synopsis'
        synopses = self.df['synopsis'].tolist()
        model = SentenceTransformer(self.model_name) 
        # Compute embeddings for each synopsis
        return model.encode(synopses, convert_to_tensor=True)
    
    def save(self, filename):
        # You can convert it to a numpy array if needed:
        embeddings_np = embeddings.cpu().numpy()

        np.savez('synopsis_embeddings.npz', embeddings=embeddings_np)
        # fname = 'dataset/processed/embeddings_' + self.model_name + '.csv'
        # self.df.to_csv(fname, index=False)

