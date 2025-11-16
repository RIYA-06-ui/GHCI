import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

lemm = WordNetLemmatizer()
stop = set(stopwords.words("english"))

def clean_text(t):
    t = t.lower()
    t = re.sub(r"[^a-zA-Z0-9 ]", " ", t)
    tokens = [lemm.lemmatize(w) for w in t.split() if w not in stop]
    return " ".join(tokens)
