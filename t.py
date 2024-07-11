import pandas as pd
from sentence_transformers import SentenceTransformer
import time
import numpy as np

start = time.time()

df = pd.read_csv('dataset/modified_manga.csv')
# MODEL = 'all-mpnet-base-v2' # General-purpose, best for applications where accuracy is more important than speed.
# MODEL = 'paraphrase-MiniLM-L6-v2' # Balanced Performance. Paraphrase identification, text similarity tasks.
MODEL = 'paraphrase-mpnet-base-v2' # High-accuracy paraphrase identification and text similarity tasks. Slightly slower than MiniLM


# Assuming the column containing synopses is named 'synopsis'
synopses = df['synopsis'].tolist()

# Load a pre-trained Sentence-BERT model
model = SentenceTransformer(MODEL) 

# Compute embeddings for each synopsis
embeddings = model.encode(synopses, convert_to_tensor=True)


# Now, 'embeddings' is a tensor containing the sentence embeddings for each synopsis
# You can convert it to a numpy array if needed:
embeddings_np = embeddings.cpu().numpy()

np.savez('synopsis_embeddings.npz', embeddings_np)

# # Convert each embedding to a comma-separated string
# embeddings_str = [','.join(map(str, embedding)) for embedding in embeddings_np]

# # Add the embeddings back to the dataframe
# df['embeddings'] = embeddings_str

# # # If you want to add the embeddings back to the dataframe and save it
# # df['embeddings'] = list(embeddings_np)

# fname = 'dataset/manga_dataset_with_embeddings_' + MODEL + '.csv'

# df.to_csv(fname, index=False)

end = time.time()

print(end - start)