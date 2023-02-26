import os
from pathlib import Path
from nltk.tokenize import word_tokenize, RegexpTokenizer

path_to_writing_folder = "/Users/mbarry/Documents/03_hobbies/writing/prose/essays"
os.listdir(path_to_writing_folder)

text_content = ""
file_count = 0
for path in Path(path_to_writing_folder).rglob("*.txt"):
    with open(path, "r") as read_file:
 
        text_content += read_file.read().replace("\n", ' ')
        print(text_content)
    file_count += 1
    
tokenizer = RegexpTokenizer(r'\w+')
tokenized_words = tokenizer.tokenize(text_content)
tokenized_words = [word.lower() for word in tokenized_words]
