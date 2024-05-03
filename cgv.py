import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 현재 날짜, 시간 구하기
now = time.strftime('%Y-$m_%d_%H_%M')

result_pass_list = [] #pass한 TC ID를 가지고 있는 리스트
result_fail_list = [] #fail한 TC ID를 가지고 있는 리스트
result_reason_list = [] #fail한 원인을 가지고 있는 리스트
tc_count = 15 #전체 TC 개수 카운트

# 테스트 전 과정에 걸쳐 에러발생 시 에러기록하는 try, except문 
# f = open(f'test_result/{now}_test_result.txt', 'w')
# f.write(f'테스트 수행 일자 - {now}\n')

try: 

  # TC cgv_01 cgv 홈페이지 접속 
  tc_progress = 'cgv_01'
  driver = webdriver.Chrome()
  driver.get('https://www.cgv.co.kr')
  driver.implicitly_wait(10)
  driver.maximize_window()
  print('##################테스트 시작###################')
  print('cgv_01 cgv홈페이지 접속 성공')
  print(driver.title)
  print(driver.current_url)

  # TC cgv_02 로그인 버튼 확인, 클릭
  try:
    if driver.find_element(By.CSS_SELECTOR, '#cgvwrap > div.header > div.header_content > div > ul > li:nth-child(2) > a > img').is_displayed():
      print('TC_02_1 로그인 버튼 노출')
      result_pass_list.append(tc_progress)
      time.sleep(2) # 인터렉션 지연

      try:
        driver.find_element(By.XPATH, '//*[@id="cgvwrap"]/div[2]/div[1]/div/ul/li[1]/a').click()
        print('TC_02_2 로그인 버튼 클릭')
        result_pass_list.append(tc_progress)
        time.sleep(5)

      except Exception as e:
        fail_reason = '로그인 페이지 진입 실패'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        result_reason_list.append(fail_reason)

  except Exception as e:
    fail_reason = '로그인 버튼 미노출'
    print(fail_reason)
    result_fail_list.append(tc_progress)
    result_reason_list.append(fail_reason)

  #cgv_03 로그인 실패
  try: 
    driver.implicitly_wait(10)
    id = driver.find_element(By.ID, 'txtUserId')
    id.click()
    id.send_keys('pso0244')
    time.sleep(2)

    driver.implicitly_wait(10)
    password = driver.find_element(By.ID, 'txtPassword')
    password.click()
    password.send_keys('dddd')
    time.sleep(2)

    driver.find_element(By.XPATH, '//*[@id="submit"]').click()
    time.sleep(2)
    Keys.RETURN()

    print('TC_03 로그인 실패')
    result_pass_list.append(tc_progress)

  except Exception as e:
    fail_reason = '로그인 오류 테스트 실패'
    print(fail_reason)
    result_fail_list.append(tc_progress)
    result_reason_list.append(fail_reason)

except Exception as e:
  print('에러가 발생하여 테스트 종료:', e)
  driver.quit()
  sys.exit(1)

finally:
  print('##########테스트 스크립트 종료.##########')
  driver.quit()