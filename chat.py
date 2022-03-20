
import random
import numpy as np
import json
from nltk_utils import tokenize, stem, bag_of_words
from train import xy, ignore_words
from tag import get_tag

with open('intents.json','r') as f:
    intents=json.load(f)

bot_name="Quilty"
print("Let's chat! type 'quit' to exit")

def get_response(input):
    
    sentence=tokenize(input)
    sentence=[stem(w) for w in sentence if w not in ignore_words]
    tag=get_tag(sentence)
    print(sentence)
    response=[]
    for intent in intents["intents"]:
        if tag==intent["tag"]:
            response.append(random.choice(intent['responses']))
            # print(f"{bot_name}: {random.choice(intent['responses'])}")
        
    if len(response)==0:
        print(f"{bot_name}: I do not understand...")
        
    else:
        print(f"{bot_name}: {response[0]}")
        


# print(all_words)
while True:
    sentence=input('You: ')
    sentence.lower()
    if sentence=='quit':
        break
    else:
        get_response(sentence)

