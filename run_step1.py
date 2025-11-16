from pipeline.data_loader import load_data
from pipeline.preprocess import preprocess
from embeddings.combine import generate_final_embeddings
from pipeline.save import save_outputs

# STEP 1 RUNNER
df = load_data("raw_data.csv")
df = preprocess(df)
embeddings = generate_final_embeddings(df)
save_outputs(df, embeddings)

print("STEP 1 COMPLETED ✔ Clean data + Embeddings saved")


