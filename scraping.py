#use request module
# use bs4 module(Beautifulsoup)

import requests
from bs4 import BeautifulSoup
import csv

url = input("Enter a  web page URL you want to scrap: ")

r=requests.get(url)
# print(r.text)


soup=BeautifulSoup(r.text,"html.parser")
headlines=[]

for i in soup.find_all(['head','h1','h2','h3','h4']):
    text=i.get_text(strip=True)
    if text:
        headlines.append(text)

paragraphs=[]
for i in soup.find_all(['p']):
    text=i.get_text(strip=True)
    if text:
        paragraphs.append(text)

print("\n-----headlines:------\n")

for h in headlines:
    print(h)


print("\n-----paragraphs:------\n")

for p in headlines:
    print(p)

with open("file.txt","w") as f:
    f.write("headlines\n")
    for h in headlines:
        f.write(h+'\n')

    f.write("paragraphs\n")
    for p in paragraphs:
        f.write(p+'\n')

with open("file.csv","w") as f:
    writer=csv.writer(f)
    writer.writerow(["type","content"])
    for h in headlines:
        writer.writerow(["headlines", h])

    for p in paragraphs:
        writer.writerow(["paragraphs", p])


print("\nData stored succseefully")






    