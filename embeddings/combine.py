import numpy as np
from .sbert_embed import get_sbert_embeddings

def generate_final_embeddings(df):
    # Only SBERT embeddings
    sbert_vecs = get_sbert_embeddings(df["clean"].tolist())
    return sbert_vecs
