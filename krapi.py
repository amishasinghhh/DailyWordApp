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

sys.stdout = open("krtranswords.txt", "w", encoding="utf-8")
for word in newLine.split():
    url = "https://krdict.korean.go.kr/api/search?certkey_no=3971&key=92425B7F6398BF034955A47FC88B8D6B&type_search=search&part=word&q="
    url2 = "&sort=popular&translated=y&trans_lang=1"
    response = requests.get(url = url + word + url2, verify=False)
    root = ET.fromstring(response.text)
    tree = ET.ElementTree(root)
    tree.write("data.xml", encoding="UTF-8")
    transWord = tree.find('.//trans_word').text
    print(transWord)


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
