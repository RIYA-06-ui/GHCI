from .cleaner import clean_text

def preprocess(df):
    df["clean"] = df["text"].apply(clean_text)
    return df
