from pathlib import Path

from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize

from summary_statistics import count_words

class Corpus:

    def __init__(self, path_to_documents_folder):

        self.path_to_documents_folder = path_to_documents_folder
        self.documents = {}
        self.document_count = 0
        self.read_in_documents()
        self.corpus_string = self.create_corpus_string()
        self.word_count = count_words(self.corpus_string)
        self.document_tokens = []
        

    def read_in_documents(self, doctype="txt"):

        """ 
        Read in all documents of the given doctype
        and store them in the document dicionary
        """
        for path in Path(self.path_to_documents_folder).rglob(f"*.{doctype}"):
            with open(path, "r") as read_file:
                document_string = read_file.read().replace("\n", " ")
                self.documents[path.name] = document_string
        
        self.document_count = len(self.documents)
        print(f"There are {self.document_count} documents in the corpus")
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
        tokenizer = RegexpTokenizer(r"\w+")
        tokenized_words = tokenizer.tokenize(self.corpus_string)
        tokenized_words = [word.lower() for word in tokenized_words]

        if remove_stop_words:
            tokenized_words = [
                word for word in tokenized_words 
                if word not in stopwords.words("English")
            ]
            self.document_tokens = tokenized_words
            return tokenized_words
        
        else:
            self.document_tokens = tokenized_words
            return tokenized_words



class Document:

    def __init__(self, path_to_document):

        self.path_to_document = path_to_document
        self.document_name = ""
        self.document_string = ""
        self.read_in_document()
        self.sentences = []
        self.create_sentences()

    
    def read_in_document(self):
        
        """
        Read in a document given a path to the document
        """
        
        # create Path object to allow access to document name
        doc_path = Path(self.path_to_document)

        with open(Path(doc_path), "r") as read_file:
            self.document_string = read_file.read().replace("\n", " ")
            self.document_name = doc_path.name
                   

    def create_sentences(self):

        # TODO Figure out how to parse the date stamps of a journal entry
        tokenized_sentences = sent_tokenize(self.document_string)
        self.sentences = [Sentence(sentence_string) for sentence_string in tokenized_sentences]


class Sentence:

    """
    Take a sentence string and describe it:
        Length
        Number of words
        Type of sentence based on punctuation

    """

    def __init__(self, sentence_string):
        
        self.sentence_string = sentence_string
        self.word_tokens = []
        self.word_tokenize()
        self.punctuation_marks = []
        self.find_punctuation_marks()
        self.type_of_sentence = ""
        self.determine_type_of_sentence()
        self.string_length = len(self.sentence_string)
        self.word_count = len(self.word_tokens)
        
    
    def word_tokenize(self):
        
        tokenizer = RegexpTokenizer(r"\w+")
        self.word_tokens = tokenizer.tokenize(self.sentence_string)

    
    def find_punctuation_marks(self):

        
        # find elipses first, so that the match doesn"t stop after a period
        tokenizer = RegexpTokenizer(r"\.{3}|[!,;:?.]")
        self.punctuation_marks = tokenizer.tokenize(self.sentence_string)
        
    
    def determine_type_of_sentence(self):


        sentence_types = {
            ".": "declarative",
            "?": "question",
            "!": "exclamation"}
        
        # determine the sentence type by the last punctuation token
        if self.punctuation_marks[-1] in sentence_types:
            self.type_of_sentence = sentence_types[self.punctuation_marks[-1]]
        else:
            self.sentence_type = "undefined"


