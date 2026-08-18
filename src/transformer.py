from sentence_transformers import SentenceTransformer
import matplotlib.pyplot as plt

# Load the pre-trained Sentence Transformers model — downloads once, then cached locally
model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = [
    "I am a happy person.",
    "I am a joyful person.",
    "I am a pessimistic person.",
    "I am not an optimistic person."
]

# Generate embeddings for the sentences
embeddings = model.encode(sentences)

print(embeddings.shape)          # (4, 384) — 4 sentences, 384 dimensions each
print(embeddings[:, :5])         # first 5 dimensions of each, just to peek