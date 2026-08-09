from sentence_transformers import SentenceTransformer

# Load the pre-trained Sentence Transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = [
    "I am a happy person.",
    "I am a joyful person.",
    "I am a pessimistic person.",
    "I am not an optimistic person."
]

# Encode sentences into embeddings
embeddings = model.encode(sentences)

# Compute the cosine similarity between the embeddings
similarity_matrix = model.similarity(embeddings, embeddings)
print(similarity_matrix)