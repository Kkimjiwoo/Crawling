from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])
driver = webdriver.Chrome(options=chrome_options)

path = "https://www.google.com/search?q=samsung+stock+price" # 경로 지정
driver.get(path)

company_element = driver.find_element(By.CLASS_NAME, 'DoxwDb')
price_element = driver.find_element(By.CSS_SELECTOR, '.IsqQVc.NprOob.wT3VGc')
company = company_element.text
price = price_element.text

print(f"{company}의 현재 주가는 {price}원 입니다.")

driver.quit()