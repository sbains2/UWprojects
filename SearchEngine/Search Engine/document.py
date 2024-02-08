"""
Sahil Bains
CSE 163 Section AG
document.py
"""

from cse163_utils import normalize_token


class Document:
    """
    This represents the data in a single document file
    """
    def __init__(self, path: str) -> None:
        """
        This is the initializer for the Document class.
        It creates a private
        """
        self._path = path
        with open(path, encoding='UTF-8') as f:
            chunk = f.read().lower()
        tokens = chunk.split()
        token_result = {}
        for token in tokens:
            token = normalize_token(token)
            if token not in token_result:
                token_result[token] = 0
            token_result[token] += 1
        final_chunk = sum(token_result.values())
        self._terms_freq = {token: count/final_chunk for token,
                            count in token_result.items()}

    def term_frequency(self, term: str) -> float:
        """
        Calculates the frequency of a term inputted
        """
        norm_term = normalize_token(term)
        return self._terms_freq.get(norm_term, 0)

    def get_path(self) -> str:
        """
        Returns the file path of the document
        """
        return self._path

    def get_words(self) -> list[str]:
        """
        Returns a list of the unique words in the document
        """
        return [token for token, freq in self._terms_freq.items() if freq > 0]

    def __str__(self) -> str:
        """
        This returns a string representation of the doc, including the
        file path and the number of words that it contains.
        """
        with open(self._path) as f:
            amt_words = len(f.read().split())
        return f"Document({self._path}, words: {amt_words})"