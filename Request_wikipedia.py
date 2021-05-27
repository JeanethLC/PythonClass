import requests
from lxml import html

print ("Escribe un nombre:")
nombre = input()

r = requests.get('https://es.wikipedia.org/wiki/'+ nombre +'_(nombre)')

print(r.url)
#print(r.text)

tree = html.fromstring(r.content)

gender = tree.xpath('//a[@title="Identidad sexual"]/text()')
arraygender = tree.xpath('//div[@class="mw-parser-output"]//table//tbody//td//text()')
footer = tree.xpath('//div[@class="action-list"]//p/text()')

print(gender)
#print(arraygender[3])
for i in arraygender:
    if (i.strip() == "Masculino"):
        print("Masculino")
    elif (i.strip() == "Femenino"):
        print("Femenino")