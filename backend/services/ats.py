from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re


def preprocess_text(text):
    """
    Clean and preprocess text
    """

    text = text.lower()

    # Remove special characters
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text


def calculate_ats_score(resume_text, job_description):
    """
    Calculate ATS similarity score between
    resume and job description
    """

    # Check empty input
    if not resume_text or not job_description:
        return 0

    # Preprocess texts
    resume_text = preprocess_text(resume_text)
    job_description = preprocess_text(job_description)

    # Create document list
    documents = [resume_text, job_description]

    # TF-IDF Vectorizer
    tfidf = TfidfVectorizer(
        stop_words='english',
        ngram_range=(1, 2),
        max_features=5000
    )

    # Convert text to vectors
    tfidf_matrix = tfidf.fit_transform(documents)

    # Calculate cosine similarity
    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )

    # Convert to percentage
    score = round(float(similarity[0][0]) * 100, 2)

    return score