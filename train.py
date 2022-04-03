
import random

import json
from nltk_utils import tokenize, stem, bag_of_words

# import torch
# import torch.nn as nn
# from torch.utils.data import Dataset, DataLoader
# from model import NeuralNet
ignore_words=['?','!','.',',','@','#',"$"]

with open('intents.json','r') as f:
    intents=json.load(f)

# print(intents)
all_words=[]
tags=[]
patterns=[]
xy={}

for intent in intents['intents']:
    tag=intent['tag']
    tag=tag.lower()
    tags.append(tag)
    
  
    for pattern in intent['patterns']:
        xy[pattern]=tag
        w=tokenize(pattern)
        all_words.extend(w)
        pattern=pattern.lower()
        patterns.append(pattern)
        xy[pattern]=tag
        # stems=[stem(w) for w in patterns if w not in ignore_words]
        # for i in stems:
        #     xy[i]=tag
        
        


# all_words=[stem(w) for w in all_words if w not in ignore_words]
# all_words=sorted(set(all_words))
# tags= sorted(set(tags))
# print(xy)
# print(patterns)
# print(tags)

# X_train=[]
# Y_train=[]
# for (pattern_sentence, tag) in xy:
#     bag=bag_of_words(pattern_sentence, all_words)
#     X_train.append(bag)
#     label=tags.index(tag)
#     Y_train.append(label)

# X_train=np.array(X_train)
# Y_train=np.array(Y_train)

# print(X_train)
# print(Y_train)
