from pathlib import Path
from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk.corpus import stopwords

class Corpus:

    def __init__(self, path_to_documents_folder):

        self.path_to_documents_folder = path_to_documents_folder
        self.documents = {}
        self.read_in_documents()
        self.document_count = 0
        self.corpus_string = self.create_corpus_string()

        
    def read_in_documents(self, doctype='txt'):

        """ 
        Read in all documents of the given doctype
        and store them in the document dicionary
        """
        for path in Path(self.path_to_documents_folder).rglob(f"*.{doctype}"):
            with open(path, "r") as read_file:
                document_string = read_file.read().replace("\n", " ")
                self.documents[path.name] = document_string
        
        self.document_count = len(self.documents)
        return self.documents
    
    def create_corpus_string(self):
        
        """
        Create 1 long string of all document text
        """

        corpus_string = ""
        for document in self.documents.values():
            corpus_string += document

        return corpus_string


    def tokenize_corpus(self, remove_stop_words=False):
        
        """
        Create a set of word tokens from
        the corpus string
        """

        # Use Regex tokenizer to remove numbers and punctuation.
        tokenizer = RegexpTokenizer(r'\w+')
        tokenized_words = tokenizer.tokenize(self.corpus_string)
        tokenized_words = [word.lower() for word in tokenized_words]

        if remove_stop_words:
            tokenized_words = [
                word for word in tokenized_words 
                if word not in stopwords.words("English")
            ]
            return tokenized_words
        
        else:
            return tokenized_words
        