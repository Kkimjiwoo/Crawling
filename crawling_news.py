# 뉴스을 편찬한 언론사와 내용 가져오기

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])
driver = webdriver.Chrome(options=chrome_options)

'''
key = "멀티캠퍼스"
path = f"   =={key}"
driver.get(path)

OR

driver.get("   ")
'''


#keyword = "input("키워드를 입력하세요. ")"
#driver.get(f"https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=={keyword}")
driver.get("https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query=멀티캠퍼스")
# https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%A9%80%ED%8B%B0%EC%BA%A0%ED%8D%BC%EC%8A%A4

title_list = driver.find_elements(By.CLASS_NAME,'news_tit')
company_group = driver.find_elements(By.CLASS_NAME, 'info.press')
contents = driver.find_elements(By.CLASS_NAME,'news_dsc')


for title, company, content in zip(title_list[:2],company_group[:2], contents[:2]):
    print(title.text)
    print(company.text)
    print(content.text)
   

driver.quit()
