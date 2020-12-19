from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests
import operator 
from collections import Counter

def start(soup): 
    wordlist = []
    for each_text in soup.findAll('div', {'class':'innner-page-main-about-us-content-right-part'}): 
        content = each_text.text 
        words = content.lower().split() 
          
        for each_word in words: 
            wordlist.append(each_word) 
        clean_wordlist(wordlist) 
    
    # for each_text in soup.findAll('div', {'class':'ReleaseDateSubHeaddateTime'}): 
    #     print(each_text.text.split('\n')[2].strip())
        

def clean_wordlist(wordlist): 
    print(wordlist)
    # count = 0
    # for word in wordlist:
    #     if word == 'economy' or word == 'economical':
    #         count += 1
    # print(count)



def run_script(url):
    BASE_URL = url
    with requests.Session() as session:
        response = session.get(BASE_URL)
        soup = BeautifulSoup(response.content, 'html.parser')
        # print(soup)
        for frame in soup.select("div iframe"):
            frame_url = urljoin(BASE_URL, frame["src"])
            response = session.get(frame_url)
            frame_soup = BeautifulSoup(response.content, 'html.parser') 
            start(frame_soup)

links = [
    'https://pib.gov.in/PressReleseDetail.aspx?PRID=1681386',
    'https://pib.gov.in/PressReleseDetail.aspx?PRID=1680852',
    'https://pib.gov.in/PressReleseDetail.aspx?PRID=1680298',
    'https://pib.gov.in/PressReleseDetail.aspx?PRID=1680198',
    'https://pib.gov.in/PressReleseDetail.aspx?PRID=1680021',
    'https://pib.gov.in/PressReleseDetail.aspx?PRID=1679941'
]

for link in links:
    run_script(link)