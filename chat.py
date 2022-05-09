
import random

import json
from nltk_utils import tokenize, stem, bag_of_words
from train import xy, ignore_words
from tag import get_tag
from speak import SpeakText

with open('intents.json', 'r') as f:
    intents = json.load(f)

# bot_name = "Claire"


def get_response(input):

    sentence = tokenize(input)
    sentence = [stem(w) for w in sentence if w not in ignore_words]
    tag = get_tag(sentence)
    # print(sentence)
    response = []
    for intent in intents["intents"]:
        if tag == intent["tag"]:
            response.append(random.choice(intent['responses']))
            # print(f"{bot_name}: {random.choice(intent['responses'])}")

    if len(response) == 0:
        return ("I do not understand...")
        # SpeakText("I do not understand")

    else:
        reply=response[0]
        # SpeakText(reply)
        response.clear()
        return (reply)
        
    


# print(all_words)
if __name__ == "__main__":
    print("Let's chat! type 'quit' to exit")
    while True:
        sentence = input()
        sentence.lower()
        if sentence == 'quit':
            break
        else:
            print(get_response(sentence))
