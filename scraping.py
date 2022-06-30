from turtle import left
import requests
import sys
from bs4 import BeautifulSoup


URL = "https://www.topikguide.com/6000-most-common-korean-words-1"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id='wrapper')
table = results.find("div", class_="tve_shortcode_rendered")
filePath = 'intermediate.txt'
sys.stdout = open(filePath, "w", encoding="utf-8")
word = 'align'
for x in table:
    if x.find("td") :
        x = x.text.strip()
        print(x)
sys.stdout = open("intermediate2.txt", "w", encoding="utf-8")
sys.stdin = open (filePath, "r", encoding="utf-8")
while True:
    line = sys.stdin.readline()
    if len(line.strip())!=0:
        print(line.strip())
    if not line:
        break  
sys.stdin = open("intermediate2.txt", "r", encoding="utf-8")
sys.stdout = open("krwords.txt", "w", encoding="utf-8")
count=0
while True:
    line = sys.stdin.readline()
    count+=1
    if count%3==2:
        print(line.strip())
    if not line:
        break

    URL = "https://www.topikguide.com/6000-most-common-korean-words-1"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id='wrapper')
table = results.find("div", class_="tve_shortcode_rendered")
filePath = 'intermediate.txt'
sys.stdout = open(filePath, "w", encoding="utf-8")
word = 'align'
for x in table:
    if x.find("td") :
        x = x.text.strip()
        print(x)
sys.stdout = open("intermediate2.txt", "w", encoding="utf-8")
sys.stdin = open (filePath, "r", encoding="utf-8")
while True:
    line = sys.stdin.readline()
    if len(line.strip())!=0:
        print(line.strip())
    if not line:
        break  
sys.stdin = open("intermediate2.txt", "r", encoding="utf-8")
sys.stdout = open("krwords.txt", "w", encoding="utf-8")
count=0
while True:
    line = sys.stdin.readline()
    count+=1
    if count%3==2:
        print(line.strip())
    if not line:
        break