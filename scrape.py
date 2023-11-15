import string
import json
import requests
from bs4 import BeautifulSoup

HOST = "https://www.compart.com"
PRINTABLE = string.printable

def get_unicode_ord(char):
    return f"U+{ord(char):04X}"


def scrape_related_urls(char):
    print(f"Scraping {char}...")
    ord_char = get_unicode_ord(char)
    res = requests.get(f"{HOST}/en/unicode/{ord_char}")
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, 'html.parser')    
        links = soup.find_all('a', class_='content-item card')
        return [f"{HOST}{link.get('href')}" for link in links]


def scrape_utf8(url):
    print(f"Scraping {url}...")
    res = requests.get(url)
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, 'html.parser')
        utf_char = soup.find('span', class_='box')
        if utf_char:
            utf_char = utf_char.text
        utf8_td = soup.find('td', string='UTF-8 Encoding:')
        if utf8_td:
            next_td = utf8_td.find_next_sibling('td')
            if next_td:
                print(f"Found {utf_char} at {next_td.text}")
                url_encoded_char = next_td.text.replace(' ', '').replace('0x', '%')
                char_dict[char].append([utf_char, url_encoded_char])


char_dict = {}

for char in PRINTABLE:
    char_dict[char] = []
    related_urls = scrape_related_urls(char)

    if related_urls is None:
        print("No related urls")
        exit()

    for url in related_urls:
        scrape_utf8(url)


print(json.dumps(char_dict, ensure_ascii=False))

with open('utf8.json', 'w') as f:
    json.dump(char_dict, f, ensure_ascii=False)