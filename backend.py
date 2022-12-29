import json
from difflib import get_close_matches


data = json.load(open('data.json'))

def translate(word):
    word = word.lower()
    global warning
    if word in data.keys():
        warning = ''
        return data[word]
    elif len(get_close_matches(word,data.keys())) > 0 :
        opt = list()
        warning = "We didn't completely get your word, but below are some related words:\n "
        for x , y in enumerate(get_close_matches(word,data.keys())):
              opt +=(''+get_close_matches(word,data.keys())[x]+':', data[y])
        return(opt)
    else:
          return "Sorry! We could'nt find the word you searched " 

