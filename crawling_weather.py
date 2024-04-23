'''셀레니움으로 오늘의 날씨 가져오기'''

'''
코드 스니펫- 셀레니움 뼈대 코드
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])
driver = webdriver.Chrome(options=chrome_options)

path = "https://www.google.com/search?q=weather" # 경로 지정
driver.get(path)
'''
## 셀리니움으로 클로링 코드 작성하기
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# 브라우저 옵션 설정
chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
# 브라우저를 자동화한 후 >> browser window 창 유지
chrome_options.add_experimental_option("excludeSwitches",["enable-logging"]) 
# excludeSwitches: 불필요한 로깅 메세지 >> 브라우저에서 제외

driver = webdriver.Chrome(options=chrome_options)

# 원하는 웹페이지로 이동
path = "https://www.google.com/search?q=weather"
driver.get(path)
# 터미널에 python weather(파일 명).py입력

# css 선택자 사용, 원하는 클래스를 가진 웹 요소 접근 
# #wob_tm, #oFNiHe > omnient-visibility-control > div > div > div.eKPi4.BUSxSd > span:nth-child(2) > span.BBwThe

# 온도와 관련된 정보의 선택자
element = driver.find_element(By.ID, 'wob_tm').text
# class의 값 들고 오기

# print(element)

# 위치와 관련된 정보의 선택자
location = driver.find_element(By.CSS_SELECTOR, 'span.BBwThe').text
# CLASS_NAME 이든 CSS_SELECTOR 둘다 사용 가능 
# CLASS_NAME은 명확해야함

print("-" * 30)
print(f"현재 {location}의 온도는 {element}도 입니다.")

driver.quit()

