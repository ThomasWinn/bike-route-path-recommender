import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer

class Embeddings:
    def __init__(self, model_name, dataframe):
        self.model_name = model_name
        self.df = dataframe

    def encode(self, summaries: list):
        """Encode the synopsis using the specified model name

        Args:
            summaries (list): list of txt synopsis 

        Returns:
            np.array: encoded synopses
        """
        # Assuming the column containing synopses is named 'synopsis'
        model = SentenceTransformer(self.model_name) 
        # Compute embeddings for each synopsis
        return model.encode(summaries, convert_to_tensor=True)
    
    def load(self, filename: str):
        """Load embeddings from a file

        Args:
            filename (str): file path containing the embeddings

        Returns:
            np.array: embedded synopses
        """
        npz_file = np.load(filename)
        return npz_file['embeddings']
    
    def save(self, embeddings, filename):
        """Save embeddings to a npz file

        Args:
            embeddings (np.array): np.array of embeddings 
            filename (str): file path to save npz file to
        """
        # You can convert it to a numpy array if needed:
        embeddings_np = embeddings.cpu().numpy()

        np.savez(filename, embeddings=embeddings_np)

