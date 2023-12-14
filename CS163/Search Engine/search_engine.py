"""
Sahil Bains
CSE 163 - Section AG
search_engine.py

"""
import os
from document import Document
import math
import re


class SearchEngine:
    """
    This represents a corpus of document objects
    """
    def __init__(self, paths: str) -> None:
        """
        This initializes the SearchEngine to take
        a string path to the given directory. Makes
        a dictionary where the keys are the terms and
        the values are the paths to the original corpus.
        """
        self.path = paths
        self.documents = []
        self.inverted_index = {}
        for f in os.listdir(paths):
            doc_path = os.path.join(paths, f)
            doc = Document(doc_path)
            self.documents.append(doc)
            for word in doc.get_words():
                if word not in self.inverted_index:
                    self.inverted_index[word] = [doc]
                if doc not in self.inverted_index[word]:
                    self.inverted_index[word].append(doc)
        self.num_docs = len(self.documents)

    def _calculate_idf(self, word: str) -> float:
        """
        Takes a string as a paramater then returns the
        inverse document frequency of that word. If the
        word isn't found, the IDF value is 0.
        """
        docs_containing = self.inverted_index.get(word, [])
        number_docs_containing = len(docs_containing)
        if number_docs_containing == 0:
            return 0
        else:
            return math.log(self.num_docs / number_docs_containing)

    def __str__(self) -> str:
        """
        Returns a string of the SearchEngine object
        """
        return f"SearchEngine({self.path}, size: {len(self.documents)})"

    def search(self, query: str) -> list[str]:
        """
        This takes a single or multi word query as
        an argument then normalizes the string. It
        then returns a list of the doc paths containing
        the terms and sorts them by its TF-IDF rate.
        """
        normal_q = query.lower()
        tokens = normal_q.split(' ')
        tf_idf_ = []
        for term in tokens:
            term = re.sub(r'\W+', '', term)
            if term in self.inverted_index.keys():
                for doc in self.inverted_index[term]:
                    tf = doc.term_frequency(term)
                    idf = self._calculate_idf(term)
                    tf_idf = tf * idf
                    tf_idf_.append((doc, tf_idf))
        plus_dict = {}
        for tupl in tf_idf_:
            if tupl[0] not in plus_dict:
                plus_dict[tupl[0]] = tupl[1]
            else:
                plus_dict[tupl[0]] += tupl[1]

        sorted_list = sorted(plus_dict.items(), key=lambda x: x[1],
                             reverse=True)
        sorted_list = dict(sorted_list)
        expected = [doc.get_path() for doc in sorted_list.keys()]
        return expected