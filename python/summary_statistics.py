

def count_words(corpus: str):
    
    """
    Count the number of total words in a corpus
    using a simple split on white space 
    to differentiate words
    """
    
    words = corpus.split()
    word_count = len(words)
    print(f"There are {word_count} words in the corpus")
    
    return word_count