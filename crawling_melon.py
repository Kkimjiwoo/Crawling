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

url = 'https://www.melon.com/chart/week/index.htm'
driver.get(url)

# HTML 다운로드 및 bs4로 읽기
from bs4 import BeautifulSoup
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
# tbody >> tr
songs = soup.select('tr')[1:]   # 0부터 하면 빈 칸으로 나옴
#print(songs)

# 제목 가수 추출
#title = song.select('div.ellipsis.rank01 > span > a')
#print(title)

song_data = []
rank = 1

for song in songs :
    title = song.select('div.ellipsis.rank01 > span > a')[0].text   # 곡
    singer =  song.select('div.ellipsis.rank02 > a')[0].text        # 가수
    print(title, singer, sep=',')
    mylist=['melon', rank, title, singer]
    song_data.append(mylist)
    rank += 1
    
# print(song_data)

df = pd.DataFrame(song_data, columns = ['서비스업체', '순위','곡 명','가수'])
print(df)

df.to_excel('melon_rank_20240503.xlsx, index = False')