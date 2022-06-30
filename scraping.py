from turtle import left
import requests
import sys
from bs4 import BeautifulSoup

#hi
#Scrape first 1000 Words
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

<<<<<<< HEAD
#Scrape next 1000 words (1000-2000)
URL = "https://www.topikguide.com/6000-most-common-korean-words-2"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id='theme-content-section')
sys.stdout = open('intermediate.txt', "w", encoding="utf-8")
table = results.find("div", class_="section-content")
=======
    URL = "https://www.topikguide.com/6000-most-common-korean-words-1"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id='wrapper')
table = results.find("div", class_="tve_shortcode_rendered")
filePath = 'intermediate.txt'
sys.stdout = open(filePath, "w", encoding="utf-8")
word = 'align'
>>>>>>> 809063082c8c5830ccc99a9e69daf10535a86d19
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
<<<<<<< HEAD
sys.stdout = open("krwords.txt", "a", encoding="utf-8")
=======
sys.stdout = open("krwords.txt", "w", encoding="utf-8")
>>>>>>> 809063082c8c5830ccc99a9e69daf10535a86d19
count=0
while True:
    line = sys.stdin.readline()
    count+=1
<<<<<<< HEAD
    if count%3==0:
        print(line.strip())
    if not line:
        break

URL = "https://www.topikguide.com/6000-most-common-korean-words-3"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id='theme-content-section')
sys.stdout = open('intermediate.txt', "w", encoding="utf-8")
table = results.find("div", class_="section-content")
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
sys.stdout = open("krwords.txt", "a", encoding="utf-8")
count=0
while True:
    line = sys.stdin.readline()
    count+=1
    if count%3==0:
        print(line.strip())
    if not line:
        break
=======
    if count%3==2:
        print(line.strip())
    if not line:
        break
#Scrape next 1000 words
i = 2
while i<7:
    URL = "https://www.topikguide.com/6000-most-common-korean-words-2"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id='theme-content-section')
    sys.stdout = open('intermediate.txt', "w", encoding="utf-8")
    table = results.find("div", class_="section-content")
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
        if count%3==0:
            print(line.strip())
        if not line:
            break
>>>>>>> 809063082c8c5830ccc99a9e69daf10535a86d19

URL = "https://www.topikguide.com/6000-most-common-korean-words-4"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id='theme-content-section')
sys.stdout = open('intermediate.txt', "w", encoding="utf-8")
table = results.find("div", class_="section-content")
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
sys.stdout = open("krwords.txt", "a", encoding="utf-8")
count=0
while True:
    line = sys.stdin.readline()
    count+=1
    if count%3==0:
        print(line.strip())
    if not line:
        break