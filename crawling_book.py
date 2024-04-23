from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=chrome_options)

path = "https://product.kyobobook.co.kr/bestseller/online?period=001&page=1&per=50" # 경로 지정
driver.get(path)

#pord_item, prod_info, prod_author, price

books = driver.find_elements(By.CLASS_NAME,'prod_item')
#authors = driver.find_elements(By.CLASS_NAME,'prod_author')
#prices = driver.find_elements(By.CLASS_NAME,'price')

for index, book in enumerate(books):
    rank = index + 1
    title = book.find_element(By.CLASS_NAME,'prod_info').text
    author = book.find_element(By.CLASS_NAME,'prod_author').text
    price = book.find_element(By.CLASS_NAME,'price').text
    print(rank, title, author, price)

driver.quit()