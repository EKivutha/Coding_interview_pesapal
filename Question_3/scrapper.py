import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

dict = {}

print("Enter page Url: ")
url = input()
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")

words = []

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = ''.join(chunk for chunk in chunks if chunk)
# text = text.replace("/n",",")
text = text.split()
for i in text:
    words.append(i)
# print (words)
def uniqueWord(Word):
 
    if Word in dict: 
        # If the word exists in dictionary then
        # simply increase its count
        dict[Word] += 1
 
    else: 
        # If the word does not exists in
        # dictionary update the dictionary
        # and make its count 1
        dict.update({Word: 1})
# page = requests.get(URl)
# print(page.text)
for i in words:
    uniqueWord(i)
for elements in dict:
        if dict[elements] == 1:
            print(dict)