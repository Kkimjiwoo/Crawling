from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])
# 웹드라이버 설정
driver = webdriver.Chrome(options=chrome_options)


#keyword = {'삼성'}

# 웹 페이지 주소의 위치로 이동
driver.get(f"https://www.google.com/search?q=애플+주식")    # 경로 지정

# <div class="DoxwDb">    
# <div class="PZPZlf ssJ7i B5dxMb" aria-level="2" data-attrid="title" role="heading">애플</div>  </div>
# IsqQVc NprOob wT3VGc

# CSS 선택자를 사용하여 원하는 클래스를 가진 웹 요소에 접근
# 안나온다면 자식까지 가져온다
name = driver.find_element(By.CSS_SELECTOR,".DoxwDb").text
price = driver.find_element(By.CSS_SELECTOR,".IsqQVc").text
high_price = driver.find_element(By.CSS_SELECTOR,"div[data-attrid='최고']").text
low_price = driver.find_element(By.CSS_SELECTOR,"div[data-attrid='최저']").text

# 데이터 출력
print(f'주식명: {name}')
print(f'현재 가격: {price}')
print(f'최고가: {high_price}')
print(f'최저가: {low_price}')

# driver.quit()
# driver.quit()을 호출하지 않으면 webdriver 세션이 종료되지 않고,
# 브라우저가 열려 있는 상태로 남아 있게 된다
# 즉, WebDriver세션을 종료하면, 브라우저가 종료되고 selenium이 관리하는 프로세스가 정리됨


print()

# 주소 위치 이동

keyword_list = ['애플','삼성전자','sk 하이닉스']

for kw in keyword_list:
    driver.get(f"https://www.google.com/search?q={kw}+주식")

    
    name = driver.find_element(By.CSS_SELECTOR,".DoxwDb").text
    price = driver.find_element(By.CSS_SELECTOR,".IsqQVc").text
    high_price = driver.find_element(By.CSS_SELECTOR,"div[data-attrid='최고']").text
    low_price = driver.find_element(By.CSS_SELECTOR,"div[data-attrid='최저']").text

# 데이터 출력
    print(f'주식명: {name}')
    print(f'현재 가격: {price}')
    print(f'최고가: {high_price}')
    print(f'최저가: {low_price}')
    print()
    
driver.quit()
'''
애플 정보는 출력이 되는데 그 다음 삼성전자와 sk하이닉스가 출력이 안되는데 어떻게?
raise MaxRetryError(_pool, url, reason) from reason  # type: ignore[arg-type]
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='localhost', port=6456): 
Max retries exceeded with url: /session/9cad55b78b1dfd21d64196493125eaf8/url 
(Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001BC3DE0D300>: 
Failed to establish a new connection: [WinError 10061] 대상 컴 퓨터에서 연결을 거부했으므로 연결하지 못했습니다'))

driver.quit() 위치 확인하고 WebDeiver 세션이 종료되지는 않았는지 확인하기
'''