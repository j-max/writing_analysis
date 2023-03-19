# README

The code in this repo allows a writer to analyse the trends of their writing.  It assumes that a write keeps their writing together in a folder that grows over time.   

If they have a folder on their computer with .txt files, the code will read the files and visualize the most common words.

The Corpus class found in the documents.py module allows the user to explore the text easily.

# MVP Dashboard
    1. Word counts
        - Total words
        - New words over time
        - Most frequent words
    2. Sentence patterns
        - Most frequent sentence pattern
    3. Sentiment
        - Sentiment change over time, based on seqential sentences, as opposed to time stamps.

# Classes
## Sentence Class
Then Sentence is the foundational on which the subsequent classes are built.

## Document Class
Documents are composed of sentences.
The document as a whole is also stored as a single string.

By using cumulative_sentiment, you can see how your feelings progress over time.  

# Journal Class
    - Cleaning
        - Convert time stamps and remove from sentence.
    - Sentiment over time
    - Cumulative number of new words

# Timebased analysis
This code can be run each day, and will provide insight as to differences in language usage over time.



## Ideas
    - Show how many new files were created
    - How many total words are in the writing folder.
    - What were the changes in most common words over time
    - What new words were used 
    - How many words were added each day
    - Views of analysis of changes over time
    - Show histogram of:
        - document length
        - sentence length

# Objects
    Corpus
    Document
    Essay?
    Sentence
        Add compound sentence boolean?