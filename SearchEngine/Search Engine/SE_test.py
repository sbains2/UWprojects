"""
Sahil Bains
CSE 163 - Section AG
a5_test.py

This file tests classes and functions from the document.py
and search_engine.py and cross checks their functionality
through assertion tests.
"""


from document import Document
from search_engine import SearchEngine
from cse163_utils import assert_equals

docs1 = Document('/home/corpus/test1.txt')
docs2 = Document('/home/corpus/test2.txt')
docs3 = Document('/home/corpus/test3.txt')

# Define your test functions here!


def test_init() -> None:
    """
    tests the document init function
    """
    document = docs1
    final_frequency_terms = {
        'in': 0.16666666666666666,
        'here': 0.16666666666666666,
        'is': 0.16666666666666666,
        'a': 0.16666666666666666,
        'simple': 0.16666666666666666,
        'sentence': 0.16666666666666666
    }
    assert_equals(document._terms_freq, final_frequency_terms)
    print('...initializing test: success')


def test_term_freqency() -> None:
    """
    tests the term_frequency from the Document class
    """
    document = docs1
    assert_equals(document.term_frequency('in'),
                  0.1666666666666)
    assert_equals(document.term_frequency('simple'),
                  0.1666666666666)
    print('...term frequency test: success')


def test_get_path() -> None:
    """
    Tests the get_path function from the Document class
    """
    document = docs1
    assert_equals(document.get_path(), '/home/corpus/test1.txt')
    print('...get path test: success')


def test_get_words() -> None:
    """
    Tests the get_words function from the Document class
    """
    document = docs2
    assert_equals(document.get_words(),
                  ['this', 'is', 'another',
                  'simple', 'sentence'])
    print('...get words test: success')


def test_str() -> None:
    """
    tests the __str__ function from the Document class
    """
    document = docs1
    expected_str = f"Document(/home/corpus/test1.txt, words: {24 // 4})"
    assert_equals(str(document), expected_str)
    print('...__str__ test: success')


def test_search_engine() -> None:
    """
    Function that tests the single word, multiword, and
    non-existing queries of the SearchEngine class
    """
    engine = SearchEngine('/home/corpus')

    # Single word queries
    expected = {'/home/corpus/test1.txt', '/home/corpus/test3.txt',
                '/home/corpus/test2.txt'}
    actual = set(engine.search('simple'))
    assert_equals(sorted(expected), sorted(actual))
    print('single word queries: executed')

    # Multiple word queries
    expected = {'/home/corpus/test1.txt', '/home/corpus/test3.txt',
                '/home/corpus/test2.txt'}
    actual = set(engine.search('simple sentence'))
    assert_equals(sorted(expected), sorted(actual))
    print('multiple word queries executed')

    # N/A queries
    expected = set()
    actual = set(engine.search('meep'))
    assert_equals(sorted(expected), sorted(actual))
    print('n/a queries executed')


def main():
    # Call your test functions here!
    test_init()
    test_term_freqency()
    test_get_path()
    test_get_words()
    test_str()
    test_search_engine()


if __name__ == '__main__':
    main()