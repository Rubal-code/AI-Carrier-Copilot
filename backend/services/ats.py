from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer(
    'all-MiniLM-L6-v2'
)

def calculate_ats_score(resume, jd):

    embeddings = model.encode([resume, jd])

    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )

    return round(similarity[0][0] * 100, 2)