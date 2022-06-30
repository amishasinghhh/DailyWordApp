import requests

def remove(text, target):
    if target not in text:
        return text
    start = text.find(target)
    end = start + len(target)
    text = text[:start] + text[end:]
    return remove(text, target)

with open('word_lists/sp.txt') as f:
    words = f.read().split()

partsOfSpeech = []
defns = []

i = 0
for word in words:
    if i == 50:
        break
    response = requests.get(f"https://www.dictionaryapi.com/api/v3/references/spanish/json/{word}?key=a9b5127c-2aa5-4b9d-a2ef-169551a1d086")
    for layer in response.json():
        if layer["meta"]["lang"] != "es":
            continue
        if "fl" in layer and "def" in layer:
            partsOfSpeech.append(layer["fl"])
            definition = layer["def"]
            definition = definition[0]
            haha = definition["sseq"][0][0][1]["dt"][0][1]
            start = haha.find("bc")
            defn = haha[start+3:]
            defn = remove(defn, "{a_link|")
            defn = remove(defn, "}")
            defns.append(defn)
            break
    i += 1

with open('sp_partsofspeech.txt', 'w') as f:
    for line in partsOfSpeech:
        f.write(line)
        f.write('\n')

with open('sp_defns.txt', 'w') as f:
    for line in defns:
        f.write(line)
        f.write('\n')