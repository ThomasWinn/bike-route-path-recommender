import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer

df = pd.read_csv('data/raw/manga.csv')
df = df.dropna(subset=['synopsis'])
print(df.isnull().sum())
# MODEL = 'all-mpnet-base-v2' # General-purpose, best for applications where accuracy is more important than speed.
# MODEL = 'paraphrase-MiniLM-L6-v2' # Balanced Performance. Paraphrase identification, text similarity tasks.
MODEL = 'paraphrase-mpnet-base-v2' # High-accuracy paraphrase identification and text similarity tasks. Slightly slower than MiniLM

# Assuming the column containing synopses is named 'synopsis'
df = df.dropna(subset=['synopsis'])
synopses = df['synopsis'].tolist()

# Load a pre-trained Sentence-BERT model
model = SentenceTransformer(MODEL) 

# Compute embeddings for each synopsis
embeddings = model.encode(synopses, convert_to_tensor=True)

# You can convert it to a numpy array if needed:
embeddings_np = embeddings.cpu().numpy()

np.savez('../data/embeddings/synopsis_embeddings.npz', embeddings=embeddings_np)