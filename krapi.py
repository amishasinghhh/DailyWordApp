import requests
import ssl
import certifi
from xml.etree import ElementTree as ET
import xml.dom.minidom
import sys

file = open('word_lists/kr.txt', encoding ="UTF-8")
line = file.readlines()
newLine=""
for i in line:
    if i!="\n":
        newLine+=i

#Commented out to prevent overwriting of krtranswords.txt
#Scrape trans_word
# sys.stdout = open("krtranswords.txt", "a", encoding="utf-8")
# for word in newLine.split():
#     url = "https://krdict.korean.go.kr/api/search?certkey_no=3971&key=92425B7F6398BF034955A47FC88B8D6B&type_search=search&part=word&q="
#     url2 = "&sort=popular&translated=y&trans_lang=1"
#     response = requests.get(url = url + word + url2, verify=False)
#     root = ET.fromstring(response.text)
#     tree = ET.ElementTree(root)
#     tree.write("data.xml", encoding="UTF-8")
#     transWord = tree.find('.//trans_word').text
    #print(transWord)

sys.stdout = open("krpos.txt", "w", encoding="utf-8")
for word in newLine.split():
    url = "https://krdict.korean.go.kr/api/search?certkey_no=3971&key=92425B7F6398BF034955A47FC88B8D6B&type_search=search&part=word&q="
    url2 = "&sort=popular&translated=y&trans_lang=1"
    response = requests.get(url = url + word + url2, verify=False)
    root = ET.fromstring(response.text)
    tree = ET.ElementTree(root)
    tree.write("data.xml", encoding="UTF-8")
    pos = tree.find('.//pos').text
    poseng = pos
    if pos=="전체":
        poseng="whole"
    elif pos=="명사" or pos=="의존 명사":
        poseng="noun"
    elif pos=="대명사":
        poseng="pronoun"
    elif pos=="수사":
        poseng="number"
    elif pos=="조사":
        poseng="article"
    elif pos=="동사":
        poseng="verb"
    elif pos=="형용사" or pos=="관형사" or pos=="보조 형용사":
        poseng="adjective"
    elif pos=="부사":
        poseng="adverb"
    elif pos=="감탄사":
        poseng="interjection"
    elif pos=="접사":
        poseng=="affix"
    elif pos=="어미":
        poseng="ending"
    elif pos=="품사 없음":
        poseng=="no part of speech"
    print(poseng)

# url = "https://krdict.korean.go.kr/api/search?certkey_no=3971&key=92425B7F6398BF034955A47FC88B8D6B&type_search=search&part=word&q="
# url2 = "&sort=popular&translated=y&trans_lang=1"
# response = requests.get(url = url + newLine + url2, verify=False)
# root = ET.fromstring(response.text)
# tree = ET.ElementTree(root)
# tree.write("data.xml", encoding="UTF-8")
# transWord = tree.find('.//trans_word').text
# transDef = tree.find('.//trans_dfn').text
# print(transWord)
# print(transDef)
