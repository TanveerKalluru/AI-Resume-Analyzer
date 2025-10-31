# ai-resume-analyzer/app/services/embeddings.py

from typing import List
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

class EmbeddingGenerator:
    """
    A class to generate embeddings for resumes using TF-IDF vectorization.

    Attributes:
        vectorizer (TfidfVectorizer): The vectorizer used to convert text to embeddings.
    """

    def __init__(self):
        """
        Initializes the EmbeddingGenerator with a TF-IDF vectorizer.
        """
        self.vectorizer = TfidfVectorizer()

    def generate_embeddings(self, resumes: List[str]) -> np.ndarray:
        """
        Generates embeddings for a list of resumes.

        Args:
            resumes (List[str]): A list of resume texts.

        Returns:
            np.ndarray: A 2D array of shape (n_samples, n_features) containing the embeddings.
        """
        if not resumes:
            raise ValueError("The list of resumes cannot be empty.")
        
        embeddings = self.vectorizer.fit_transform(resumes)
        return embeddings.toarray()

    def get_feature_names(self) -> List[str]:
        """
        Retrieves the feature names (terms) from the vectorizer.

        Returns:
            List[str]: A list of feature names.
        """
        return self.vectorizer.get_feature_names_out().tolist()