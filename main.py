import json


# Define a function for save the json data
def saveData(file, content):
    with open(file, "w") as f:
        f.write(json.dumps(content))


# Define a function for load all data from data.json
def loadFile(file):
    with open(file) as f:
        item = json.load(f)
    word = item[0]['word']
    meaning = item[0]['meanings'][0]['definitions'][0]['definition']
    synonyms = item[0]['meanings'][0]['synonyms']
    sound = item[0]['phonetics'][0]['audio']
    return word, sound, meaning, synonyms
