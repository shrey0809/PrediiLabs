import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk
df = pd.read_csv("Extracted.csv")
def entity_extraction(text):
    words = word_tokenize(text)
    tagged_words = pos_tag(words)
    entities = ne_chunk(tagged_words)
    return entities
df["Entities"] = df["final_col"].apply(entity_extraction)
print(df["Entities"])
