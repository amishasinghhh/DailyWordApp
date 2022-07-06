import requests
import ssl
import certifi
from xml.etree import ElementTree as ET
import xml.dom.minidom
import sys

## Commented out to prevent overwriting
## Get example sentences for words from API

# sys.stdin = open ('kr.txt', "r", encoding='utf-8')
# sys.stdout = open ('kr_examples.txt', "w", encoding="utf-8")

# for line in sys.stdin:
#   output=""
#   for x in line.split():
#     if x!="  ":
#       output+=x+" "
#   print(output)

## Commented out to prevent overwriting
## Convert Korean part of speech words to English
# sys.stdin = open("kr_partsofspeech-kr.txt", "r", encoding="utf-8")
# sys.stdout = open("kr_partsofspeech-en.txt", "w", encoding="utf-8")

# line = sys.stdin.readlines()
# newLine=""
# for i in line:
#     if i!="\n":
#         newLine+=i

# poseng=""
# for pos in newLine.splitlines():
#     if pos=="전체":
#         poseng="whole"
#     elif pos=="명사" or pos=="의존 명사":
#         poseng="noun"
#     elif pos=="대명사":
#         poseng="pronoun"
#     elif pos=="수사":
#         poseng="number"
#     elif pos=="조사":
#         poseng="article"
#     elif pos=="동사":
#         poseng="verb"
#     elif pos=="형용사" or pos=="관형사" or pos=="보조 형용사":
#         poseng="adjective"
#     elif pos=="부사":
#         poseng="adverb"
#     elif pos=="감탄사":
#         poseng="interjection"
#     elif pos=="접사":
#         poseng=="affix"
#     elif pos=="어미":
#         poseng="ending"
#     elif pos=="품사 없음":
#         poseng=="no part of speech"
#     print(poseng)

### Commented out to prevent overwriting of krtranswords.txt
### Scrape translated word
# sys.stdout = open("krtranswords.txt", "a", encoding="utf-8")
# for word in newLine.split():
#     url = "https://krdict.korean.go.kr/api/search?certkey_no=3971&key=92425B7F6398BF034955A47FC88B8D6B&type_search=search&part=word&q="
#     url2 = "&sort=popular&translated=y&trans_lang=1"
#     response = requests.get(url = url + word + url2, verify=False)
#     root = ET.fromstring(response.text)
#     tree = ET.ElementTree(root)
#     tree.write("data.xml", encoding="UTF-8")
#     transWord = tree.find('.//trans_word').text
# print(transWord)

###Commented out to prevent overwriting of krpos.txt
###Scrape part of speech
# sys.stdout = open("krpos.txt", "a", encoding="utf-8")
# for word in newLine.split():
#     url = "https://krdict.korean.go.kr/api/search?certkey_no=3971&key=92425B7F6398BF034955A47FC88B8D6B&type_search=search&part=word&q="
#     url2 = "&sort=popular&translated=y&trans_lang=1"
#     response = requests.get(url = url + word + url2, verify=False)
#     root = ET.fromstring(response.text)
#     tree = ET.ElementTree(root)
#     tree.write("data.xml", encoding="UTF-8")
#     pos = tree.find('.//pos').text
#     print(pos)
