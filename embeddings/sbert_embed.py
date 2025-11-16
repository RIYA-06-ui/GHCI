from sentence_transformers import SentenceTransformer
import numpy as np

# Load SBERT model
model = SentenceTransformer('all-MiniLM-L6-v2')

def get_sbert_embeddings(text_list):
    # Convert list of text into embeddings
    emb = model.encode(text_list, show_progress_bar=True)
    return np.array(emb)
