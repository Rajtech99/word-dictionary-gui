import json


def saveData(file, content):
    with open(file, "w") as f:
        f.write(json.dumps(content))


def loadFile(file):
    with open(file) as f:
        item = json.load(f)
    word = item[0]['word']
    sound = item[0]['phonetics'][0]['audio']
    meaning = item[0]['meanings'][0]['definitions'][0]['definition']
    synonyms = item[0]['meanings'][0]['synonyms']
    return word, sound, meaning, synonyms

