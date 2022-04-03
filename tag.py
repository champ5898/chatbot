from asyncio.windows_events import NULL
import string
import random

from train import xy, ignore_words
from nltk import tokenize, stem

ask_tag=[]

# lemmer=nltk.stem.WordNetLemmatizer()
# def LemTokens(tokens):
#     return [lemmer.lemmatize(token) for token in tokens]
# remove_punct_dict=dict((ord(punct), None) for punct in string.punctuation)
# def LemNormalize(text):
#     return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))
def freq(list):
    return max(set(list), key=list.count)

def get_tag(sentence):
    # sentence=sentence.lower()
    # sentence=list(sentence.split())
    # if input in xy.keys():
    #         tag=xy[input]
    #         ask_tag.append(tag)
    
    for i in sentence:
        if i in xy.keys():
            t=xy[i]
            ask_tag.append(t)
        
    if len(ask_tag)==0:
        return 'a'
    else:
        tag=freq(ask_tag)
        return tag
    # print(tag)
# Greetings=[]
# greeting_response=[]
# def greet(sentence):
#     for word in sentence.split():
#         if word.lower() in Greetings:
#             return random.choice(greeting_response)

# print(xy)
# y=get_tag("social protocol")
# print(y)