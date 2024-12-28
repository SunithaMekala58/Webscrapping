
#Web scrapping for xml sheet

import os
os.chdir(r"C:\Users\SUNITHA\Spyder")


import xml.etree.ElementTree as ET

tree = ET.parse("769952.xml")
root = tree.getroot()

root = ET.tostring(root, encoding='utf8').decode('utf8')

root

import re, string, unicodedata

from bs4 import BeautifulSoup

def strip_html(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()

def remove_between_square_brackets(text):
    return re.sub('\[[^]]*\]','', text)

def denoise_text(text):
    text = strip_html(text)
    text = remove_between_square_brackets(text)
    text=re.sub('  ','',text)
    return text

sample = denoise_text(root)
