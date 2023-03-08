 import os
from pathlib import Path
import sys
from nltk.tokenize import word_tokenize, RegexpTokenizer

sys.path.append("//Users/mbarry/Documents/Coding/writing_analysis/python")
from documents import Corpus

%load_ext autoreload
%autoreload 2
 
path_to_writing_folder = "/Users/mbarry/Documents/03_hobbies/writing/prose/essays"
os.listdir(path_to_writing_folder)

corpus = Corpus(path_to_writing_folder)

corpus_tokens = corpus.tokenize_corpus(remove_stop_words=True)
