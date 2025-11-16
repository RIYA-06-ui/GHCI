import pandas as pd
import numpy as np

def save_outputs(df, embeddings):
    # Save cleaned data
    df.to_csv("data/clean_data.csv", index=False)

    # Save embeddings
    np.save("embeddings/final_embeddings.npy", embeddings)

    print("Outputs saved successfully!")


