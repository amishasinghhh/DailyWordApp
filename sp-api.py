import requests
import unidecode

def remove(text, target):
    if target not in text:
        return text
    start = text.find(target)
    end = start + len(target)
    text = text[:start] + text[end:]
    return remove(text, target)

with open('word_lists/sp.txt') as f:
        words = f.read().split("\n")

words = words[1918:]

partsOfSpeech = []
defns = []
sp_sentences = []
en_sentences = []

i = 0
while i < len(words):
    word = words[i]
    print(i, word)
    response = requests.get(f"https://www.dictionaryapi.com/api/v3/references/spanish/json/{word}?key=a9b5127c-2aa5-4b9d-a2ef-169551a1d086")
    
    if response.status_code != 200 or response.json() == []:
        i += 1
        continue

    possibilities = []
    for layer in response.json():
        try:
            if "meta" in layer and "lang" in layer["meta"]:
                if unidecode.unidecode(word.strip()) in unidecode.unidecode(layer["meta"]["id"]):
                    if layer["meta"]["lang"] == "es":
                        if "fl" in layer and "def" in layer:
                            possibilities.append(layer)
        except TypeError:
            continue
    
    if possibilities == []:
        i += 1
        continue
    
    found = False
    partSpeech = ""
    firstdefn = ""
    isFirst = True
    for layer in possibilities:
        if found == True:
            break
        tmppartSpeech = layer["fl"]
        definition = layer["def"]
        definition = definition[0]
        haha = definition["sseq"][0][0][1]["dt"][0][1]
        start = haha.find("bc")
        defn = haha[start+3:]
        defn = remove(defn, "{a_link|")
        defn = remove(defn, "}")
        tmpfirstdefn = defn
        if isFirst == True:
            partSpeech = tmppartSpeech
            firstdefn = tmpfirstdefn
            isFirst = False
        vis = layer["def"][0]["sseq"]
        for sublayer in vis:
            dt = sublayer[0][1]["dt"]
            for find in dt:
                if "vis" in find:
                    found = True
                    break
            if found == True:
                sentences = find[1][0]
                sp_sentences.append(sentences["t"])
                en_sentences.append(sentences["tr"])
                partSpeech = tmppartSpeech
                firstdefn = tmpfirstdefn
                break
    
    if found == False:
        sp_sentences.append("no sentence available")
        en_sentences.append("no sentence available")
    
    partsOfSpeech.append(partSpeech)
    defns.append(firstdefn)
    
    with open('sp_spreadsheet.tsv', 'a') as f:
        line = words[i] + "\t" + partsOfSpeech[i] + "\t" + defns[i] + "\t" + sp_sentences[i] + "\t" + en_sentences[i]
        f.write(line)
        f.write("\n")
    i += 1