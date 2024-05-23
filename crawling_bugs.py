# 코드 스니펫- 셀레니움 뼈대 코드
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import numpy as np
import pandas as pd

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])
driver = webdriver.Chrome(options=chrome_options)

url = 'https://music.bugs.co.kr/chart?wl_ref=M_left_02_01'
driver.get(url)

# HTML 다운로드 및 bs4로 읽기
from bs4 import BeautifulSoup
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# tbody 내에 tr 태그 안에 p 태그
# print(soup.select('tbody>tr')[0])  >>Supernova
songs = soup.select('tbody>tr')[:99]
# print(songs)
# print(len(songs))
# song = songs[0]
# title = song.select('th > .title > a')
# print(title[0].text)

# singers = song.select('td > .artist > a')
# print(singers[0].text)

# 1-100위 차트 들어갈 리스트 초기화
song_100 = []
rank_list = []
title_list = []
singer_list = []
album_list = []
rank = 0
for song in songs:
    rank += 1
    title = song.select('th > .title > a')[0]
    singer = song.select('td > .artist > a')[0]
    album = song.select('td >a.album')[0]
    rank_list.append(f'{rank}위')
    title_list.append(title.text)
    singer_list.append(singer.text)
    album_list.append(album.text)
    
data = {'순위': rank_list, '곡': title_list, '아티스트': singer_list, '앨범': album_list}
df = pd.DataFrame(data)
print(df)
df.to_excel('bugs_rank_20240523.xlsx', index = False)

    