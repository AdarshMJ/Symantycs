# Symantycs
Symantycs is an NLP based python GUI app that allows to evaluate paper based exams.

Indian Universities largely have paper-based exams, evaluating hundreds of papers is time consuming and is prone to errors. This is an attempt to automate the boring process of paper-based evaluation. The app however is largely limited by hand-writing recognition, to circumvent this, I have used Google's Vision API to manually create a textfile consisting of key-answers and the answers by the students. I have used Spacy and NLTK to tokenize, eliminate redundant punctuations and implement a cosine similarity based framework that compares the answers written by students with the key-answers. The GUI is built using python's WxPython library.

The evaluator is asked few questions like - 

a) How much marks should be alloted if all the answers are right?
b)How much marks should be alloted if 60% of it is right?
c)How much marks should be alloted if answers are completely wrong?

1)To run the code, clone this repository.
2)Install dependencies -
a)Spacy - python -m spacy download en_core_web_sm
b)NLTK - sudo pip install -U nltk
c)WxPython - pip install -U wxPython

2)Make sure the directories for the key answers and answer scripts are properly set.
3)After all the dependencies are sucessfully installed run gui.py

