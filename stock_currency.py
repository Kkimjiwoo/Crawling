from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


chrome_options = Options()
chrome_options.add_argument("--headless")
# headless : GUI(Graphic user interface) 없이 실행
# >> 실제 브라우저 창이 눈에 보이지 않게
# >> 띄우는데도 시간이 많이 걸리기 때문에

#chrome_options.add_experimental_option("detach",True)
# headless와 상극
chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])

service = Service(excutable_path = ChromeDriverManager().install())
# selenium에서 크롬 웹 드라이버를 자동으로 다운로드 및 설치

# 웹드라이버 설정
driver = webdriver.Chrome(service=service, options=chrome_options)

wait = WebDriverWait(driver,10) # 최대한 10초 기다릴것이다

# 주소 위치 이동

keyword_list = ['애플','삼성전자','sk 하이닉스']

for kw in keyword_list:
    url =f"https://www.google.com/search?q={kw}+주가"
    
    driver.get(url)
    
    # wait
    # WebDriverWait(driver, timeout)
    # EC.presence_of_element_located : .DoxwDb가 존재할때 까지 기다릴거임 의미
    name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".DoxwDb"))).text
    price = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".IsqQVc"))).text
    high_price = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"div[data-attrid='최고']"))).text
    low_price = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"div[data-attrid='최저']"))).text
    currency = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".knFDje"))).text

#  화폐단위 표시 조건
 
    if currency == 'KRW':
        price = price + "won"
        high_price = price + "won"
        low_price = price + "won"
    elif currency == 'USD':
        price = price + "$"
        high_price = price + "$"
        low_price = price + "$"


# 데이터 출력
    print(f'{kw}주식 정보 수집 현황')
    print(f'주식명: {name}')
    print(f'현재 가격: {price}')
    print(f'최고가: {high_price}')
    print(f'최저가: {low_price} \n')

    
driver.quit()

