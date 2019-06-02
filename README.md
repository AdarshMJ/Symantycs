# Symantycs
Lexei is an intelligent paper evaluation engine. (I know the name sounds like that of a stripper!)

Indian Universities largely have paper-based exams, evaluating hundreds of papers is time consuming and is prone to errors. This is an attempt to automate the boring process of paper-based evaluation. The app however is largely limited by hand-writing recognition, to circumvent this, I have used Google's Vision API to manually create a textfile consisting of key-answers and the answers by the students. I have used Spacy and NLTK to tokenize, eliminate redundant punctuations and implement a cosine similarity based framework that compares the answers written by students with the key-answers. The GUI is built using python's WxPython library.

The evaluator is asked few questions like - 

a)How much marks should be alloted if all the answers are right?
b)How much marks should be alloted if 60% of it is right?
c)How much marks should be alloted if answers are completely wrong?

1)To run the code, clone this repository.
2)Install dependencies -
a)Spacy - python -m spacy download en_core_web_sm
b)NLTK - sudo pip install -U nltk
c)WxPython - pip install -U wxPython

2)Make sure the directories for the key answers and answer scripts are properly set.
3)After all the dependencies are sucessfully installed run gui.py

Spacy offers different language models which can be incorporated in this code. Check out their site - https://spacy.io/models
This simple GUI application can serve as an ingress for more complex operations that can be used to grade papers of different languages by incorporating the corresponding language models. The current limitation is hand-writing recogntition.

It should be possible to incorporate this implementation of handwriting recognition - https://towardsdatascience.com/build-a-handwritten-text-recognition-system-using-tensorflow-2326a3487cd5

