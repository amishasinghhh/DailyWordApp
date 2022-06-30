import requests
import ssl
import certifi
from xml.etree import ElementTree as ET
import xml.dom.minidom

file = open('word_lists/kr.txt', encoding ="utf-8")
line = file.readline()
newLine=""
for i in line:
    if i!="\n":
        newLine+=i
print(newLine)

url = "https://krdict.korean.go.kr/api/search?certkey_no=3971&key=92425B7F6398BF034955A47FC88B8D6B&type_search=search&part=word&q="
url2 = "&sort=popular&translated=y&trans_lang=1"
# r = requests.get(url =url + "것" + url2, verify=False)
# root = ET.fromstring(r.text)
# tree = ET.ElementTree(root)
# tree.write("data.xml")
doc = xml.dom.minidom.parse("data.xml")
channel = doc.firstChild
# doc = xml.dom.minidom.parse(response);
# print(doc.nodeName)

# response.raw.decode_content = True
# events = ElementTree.iterparse(response.raw)
# for event, elem in events:
#     print(elem)
    
#request2 = requests.get(url = "https://krdict.korean.go.kr/api/search?certkey_no=3971&key=92425B7F6398BF034955A47FC88B8D6B&type_search=search&part=word&q=%EB%82%98%EB%AC%B4&sort=dict", verify=False)

