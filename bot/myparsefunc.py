import requests #pip install requests
from bs4 import BeautifulSoup #pip install BeautifulSoup4
#pip install lxml


def parcecollege():
    inp_text=""
    source = requests.get('https://college.edunetwork.ru/77/?page=0').text
    soup = BeautifulSoup(source, 'lxml')
    unit = soup.findAll('p', class_="unit-name")
    inp_text+= str(unit)

    s = []
    for char in inp_text:
        s.append(char)
    s.remove("[")
    s.remove("]")
    while ">" in s:      
        tag_start = s.index('<')
        tag_end = s.index('>')
        del s[tag_start:tag_end+1]

    text = ""
    for char in s:
        text += char

    return text

def parcevuz():
    inp_text=""
    source = requests.get('https://vuz.edunetwork.ru/77/?page=0').text
    soup = BeautifulSoup(source, 'lxml')
    unit = soup.findAll('p', class_="unit-name")
    inp_text+= str(unit)

    s = []
    for char in inp_text:
        s.append(char)
    s.remove("[")
    s.remove("]")

    while ">" in s:      
        tag_start = s.index('<')
        tag_end = s.index('>')
        del s[tag_start:tag_end+1]

    text = ""
    for char in s:
        text += char

    return text
