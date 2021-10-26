# -*- coding: UTF-8 -*-
#!/usr/bin/python

import requests
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings()
import datetime

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0",
    "Content-Type": "application/x-www-form-urlencoded",
}

url = 'https://forum.ywhack.com/forum-59-1.html'
try:

    req = requests.get(url, headers=headers, verify=False, timeout=10)
    req.encoding = req.apparent_encoding
    soup = BeautifulSoup(req.text, "html.parser")
    box = soup.find('table',id="forum_59")

    list = BeautifulSoup(str(box), "lxml")

    pieces = list.findAll('tbody')
    print('#日报推送 ' + str(datetime.datetime.now().strftime("%Y-%m-%d")) + '\n')
    i = 0
    for piece in pieces:
        title = piece.find('div', class_='header_title').text.strip()
        url = piece.find('div', class_='header_title').a['href']
        tag = piece.find('span', class_='badge badge-tag').text
        for div in piece.find('div', class_='header_text'):
            fanyi = div[:-2].strip()
            break
        if title == fanyi:
            print(title + '\n' + url + ' · ' + tag  + '\n')
        else:
            print(title + '\n' + url + ' · ' + tag + '\n' + fanyi + '\n')
        i = i + 1
        if i >= 6:
            break
except Exception as e:
    print(e)